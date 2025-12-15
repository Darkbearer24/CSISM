import smtplib
from email.message import EmailMessage
from datetime import datetime, timezone
from config import (
    SMTP_SERVER,
    SMTP_PORT,
    SMTP_USERNAME,
    SMTP_PASSWORD,
    SENDER_EMAIL,
    RECEIVER_EMAIL,
)

def build_email_body(data: dict) -> str:
    lines = [
        "New ISM College Enquiry – CSISM Website",
        "",
        f"Full Name: {data.get('name', '')}",
        f"Email Address: {data.get('email', '')}",
        f"Phone Number: {data.get('phone', '')}",
        f"Name of AYUSH College: {data.get('collegeName', '')}",
        f"Inquiry Type: {data.get('inquiryType', '')}",
        f"Submission Timestamp (UTC): {data.get('timestamp', datetime.now(timezone.utc).isoformat())}",
        "",
        "This email was generated automatically by the CSISM website.",
    ]
    return "\n".join(lines)

def send_enquiry_email(data: dict):
    msg = EmailMessage()
    msg["Subject"] = "New ISM College Enquiry – CSISM Website"
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg.set_content(build_email_body(data))
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=10) as smtp:
        smtp.starttls()
        smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
        smtp.send_message(msg)

