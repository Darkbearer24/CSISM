import json
import os
import re
import smtplib
from email.message import EmailMessage
from http.server import BaseHTTPRequestHandler

ALLOWED_INQUIRY_TYPES = {
    "teacher-code",
    "running-colleges",
    "new-ayush-college",
    "court-matters",
    "appealing",
    "monetary-penalty",
    "regularization-of-batch",
    "general",
}

# Precompile regex for performance
# Matches control characters (0-31) EXCEPT \t (9), \n (10), \r (13)
CONTROL_CHARS_RE = re.compile(r'[\x00-\x08\x0B\x0C\x0E-\x1F]')

# Module-level configuration (Optimization: Load once per cold start)
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtpout.secureserver.net")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USERNAME = os.getenv("SMTP_USERNAME", "")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")
SENDER_EMAIL = os.getenv("SENDER_EMAIL", SMTP_USERNAME or "noreply@example.com")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL", SENDER_EMAIL)

try:
    SMTP_TIMEOUT = int(os.getenv("SMTP_TIMEOUT", "10"))
except (ValueError, TypeError):
    SMTP_TIMEOUT = 10

# Global SMTP client to reuse connections across warm invocations
_smtp_client = None

def sanitize_text(value: str, max_len: int = 200) -> str:
    if not isinstance(value, str):
        return ""
    v = value.strip()
    # Optimized: Truncate before processing to avoid unnecessary work
    v = v[:max_len]
    # Optimized: Use regex to remove control characters
    v = CONTROL_CHARS_RE.sub('', v)
    return v

def validate(payload: dict):
    name = sanitize_text(payload.get("name", ""))
    email = sanitize_text(payload.get("email", ""))
    phone = sanitize_text(payload.get("phone", ""))
    college = sanitize_text(payload.get("collegeName", ""))
    inquiry = sanitize_text(payload.get("inquiryType", "general"))
    if inquiry not in ALLOWED_INQUIRY_TYPES:
        inquiry = "general"
    if not name or "@" not in email:
        return False, "Invalid name or email"
    return True, {
        "name": name,
        "email": email,
        "phone": phone,
        "collegeName": college,
        "inquiryType": inquiry,
    }

def connect_smtp():
    """Establishes a new SMTP connection using module-level configuration."""
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=SMTP_TIMEOUT)
    server.starttls()
    if SMTP_USERNAME and SMTP_PASSWORD:
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
    return server

def send_email(data: dict):
    global _smtp_client

    subject = "New ISM College Enquiry – CSISM Website"
    body = "\n".join([
        "New ISM College Enquiry – CSISM Website",
        "",
        f"Full Name: {data.get('name','')}",
        f"Email Address: {data.get('email','')}",
        f"Phone Number: {data.get('phone','')}",
        f"Name of AYUSH College: {data.get('collegeName','')}",
        f"Inquiry Type: {data.get('inquiryType','')}",
        "",
        "This email was generated automatically by the CSISM website.",
    ])

    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = subject
    msg.set_content(body)

    if _smtp_client is None:
        _smtp_client = connect_smtp()

    try:
        _smtp_client.send_message(msg)
    except Exception:
        # If connection died, reconnect and retry once
        try:
            _smtp_client = connect_smtp()
            _smtp_client.send_message(msg)
        except Exception as e:
            # If it fails again, we should probably reset _smtp_client to None so next request tries fresh
            _smtp_client = None
            raise e

def json_response(handler: BaseHTTPRequestHandler, status: int, payload: dict):
    data = json.dumps(payload).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json")
    handler.send_header("Access-Control-Allow-Origin", "*")
    handler.send_header("Access-Control-Allow-Headers", "Content-Type")
    handler.end_headers()
    handler.wfile.write(data)

class handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_POST(self):
        try:
            length = int(self.headers.get("Content-Length", "0"))
            raw = self.rfile.read(length) if length > 0 else b""
            payload = json.loads(raw.decode("utf-8") or "{}")
        except Exception:
            return json_response(self, 400, {"success": False, "error": "Invalid JSON"})

        if not isinstance(payload, dict):
            return json_response(self, 400, {"success": False, "error": "Invalid request body"})

        ok, clean = validate(payload)
        if not ok:
            return json_response(self, 400, {"success": False, "error": clean})

        try:
            send_email(clean)
        except Exception:
            return json_response(self, 502, {"success": False, "error": "Unable to send email"})

        return json_response(self, 200, {"success": True})
