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

def sanitize_text(value: str, max_len: int = 200) -> str:
    if not isinstance(value, str):
        return ""
    v = value.strip()
    # Optimized: Use regex to remove control characters
    v = CONTROL_CHARS_RE.sub('', v)
    return v[:max_len]

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

def send_email(data: dict):
    smtp_server = os.getenv("SMTP_SERVER", "smtpout.secureserver.net")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    smtp_user = os.getenv("SMTP_USERNAME", "")
    smtp_pass = os.getenv("SMTP_PASSWORD", "")
    sender = os.getenv("SENDER_EMAIL", smtp_user or "noreply@example.com")
    receiver = os.getenv("RECEIVER_EMAIL", sender)
    # Default timeout to 10 seconds to prevent hanging
    try:
        timeout = int(os.getenv("SMTP_TIMEOUT", "10"))
    except (ValueError, TypeError):
        timeout = 10

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
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP(smtp_server, smtp_port, timeout=timeout) as server:
        server.starttls()
        if smtp_user and smtp_pass:
            server.login(smtp_user, smtp_pass)
        server.send_message(msg)

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
