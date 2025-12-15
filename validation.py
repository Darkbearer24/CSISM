import re

ALLOWED_INQUIRY_TYPES = {
    "teacher-code",
    "running-colleges",
    "new-ayush-college",
    "court-matters",
    "appealing",
    "monetary-penalty",
    "regularization-of-batch",
}

def sanitize_text(value: str, max_len: int = 200) -> str:
    if not isinstance(value, str):
        return ""
    v = value.strip()
    v = re.sub(r"[\x00-\x1f\x7f]", "", v)
    v = v[:max_len]
    return v

def validate_email(value: str, max_len: int = 254) -> bool:
    if not isinstance(value, str):
        return False
    v = value.strip()
    if len(v) > max_len:
        return False
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return re.match(pattern, v) is not None

def sanitize_phone(value: str) -> str:
    if not isinstance(value, str):
        return ""
    digits = re.sub(r"[^\d+]", "", value)
    return digits

def validate_and_sanitize(payload: dict):
    name = sanitize_text(payload.get("name", ""), 120)
    email = sanitize_text(payload.get("email", ""), 254)
    phone = sanitize_phone(payload.get("phone", ""))
    college = sanitize_text(payload.get("collegeName", ""), 180)
    inquiry_type = sanitize_text(payload.get("inquiryType", ""), 80)
    if not name:
        return False, "Full Name is required"
    if not email or not validate_email(email):
        return False, "Valid Email is required"
    if not phone or len(re.sub(r"[^0-9]", "", phone)) < 7 or len(re.sub(r"[^0-9]", "", phone)) > 15:
        return False, "Valid Phone Number is required"
    if not inquiry_type or inquiry_type not in ALLOWED_INQUIRY_TYPES:
        return False, "Valid Inquiry Type is required"
    clean = {
        "name": name,
        "email": email,
        "phone": phone,
        "collegeName": college,
        "inquiryType": inquiry_type,
    }
    return True, clean

