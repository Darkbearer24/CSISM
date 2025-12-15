## Overview
- Implement a small Flask backend that exposes `POST /api/enquiry`, validates and sanitizes inputs, and sends an email via GoDaddy Titan SMTP using placeholders.
- Wire the existing form in `index.html` to submit via `fetch` without page reload, show success/error messages, and preserve the current anti‑bribery modal flow.

## Backend Files
- `app.py`: Flask app with `POST /api/enquiry` that:
  - Accepts JSON body from the form
  - Validates required fields: `full_name`, `email`, `phone`, `inquiry_type`
  - Sanitizes all inputs and whitelists `inquiry_type` values to match the dropdown
  - Returns JSON: `{"success": true}` or `{"success": false, "error": "message"}`
  - Adds minimal CORS headers for `http://127.0.0.1:8000` and handles `OPTIONS` preflight (no external CORS dependency)
- `config.py`: Centralizes SMTP placeholders with clear comments:
  - `SMTP_SERVER = "smtpout.secureserver.net"`
  - `SMTP_PORT = 587`
  - `SMTP_USERNAME = "REPLACE_WITH_DOMAIN_EMAIL"`  # sender must equal username
  - `SMTP_PASSWORD = "REPLACE_WITH_EMAIL_PASSWORD"`
  - `SENDER_EMAIL = "REPLACE_WITH_DOMAIN_EMAIL"`
  - `RECEIVER_EMAIL = "REPLACE_WITH_RECEIVER_EMAIL"`
- `email_service.py`: Encapsulates SMTP send:
  - Builds a professional `EmailMessage` with subject `New ISM College Enquiry – CSISM Website`
  - Includes server‑side timestamp (UTC) and all enquiry fields in a clean body
  - Uses TLS (`starttls`), logs no credentials, sets sensible timeout, raises typed exceptions on failure
- `validation.py`: Input sanitize/validate functions:
  - `sanitize_text` (strip, remove control chars, cap length)
  - `validate_email` (basic RFC‑like regex + length cap)
  - `sanitize_phone` (digits + optional `+`, length 7–15)
  - `validate_inquiry_type` (must be one of: `teacher-code`, `running-colleges`, `new-ayush-college`, `court-matters`, `appealing`, `monetary-penalty`, `regularization-of-batch`)
  - Returns `(ok, clean_data | error_message)` used by the endpoint

## Endpoint Behavior
- Request: JSON `{ name, email, phone, collegeName, inquiryType }`
- Flow:
  - Validate/sanitize → if invalid, return `{ success: false, error }` (400)
  - Compose and send email via `email_service.send_enquiry_email(clean_data)`
  - On success: `{ success: true }` (200)
  - On SMTP errors: `{ success: false, error: "Unable to send email" }` (502)
- Security:
  - No credential logging
  - Reject oversized payloads
  - Strip HTML/JS content from text inputs
  - Code layout ready for future: DB insert, rate limiting, admin endpoints

## Frontend Wiring (Minimal JS)
- Keep the current `handleSubmit(event)` and anti‑bribery modal UX.
- Store all fields (`name`, `email`, `phone`, `collegeName`, `inquiryType`) in `window.pendingFormData` inside `handleSubmit`.
- In `closeAntiBriberyModal()`:
  - After closing the modal, call `submitEnquiry(window.pendingFormData)`
  - `submitEnquiry(...)` will `fetch('http://127.0.0.1:5000/api/enquiry', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) })`
  - Disable the submit button while sending; re‑enable after response
  - Display a non‑intrusive success or error message beneath the form; do not redesign UI
  - On success: reset the form

## Email Content
- Subject: `New ISM College Enquiry – CSISM Website`
- Body fields:
  - Full Name
  - Email Address
  - Phone Number
  - Name of AYUSH College
  - Inquiry Type
  - Submission timestamp (server‑side, UTC)

## CORS & Local Serving
- Add CORS headers in Flask (`Access-Control-Allow-Origin: http://127.0.0.1:8000`, methods `POST, OPTIONS`, headers `Content-Type`).
- Support `OPTIONS /api/enquiry` for preflight.

## Extensibility Hooks
- Clear separation of concerns: `app.py` (routing), `validation.py` (input hygiene), `email_service.py` (SMTP), `config.py` (placeholders)
- Ready to add:
  - DB persistence after email send
  - Rate limiting middleware
  - Admin dashboards with authenticated routes

## Verification
- After implementing, test via the existing page at `http://127.0.0.1:8000/`:
  - Submit valid and invalid payloads to verify validation and error messaging
  - Confirm email send path handles SMTP failures gracefully
