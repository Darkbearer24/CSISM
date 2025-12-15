from flask import Flask, request, jsonify, make_response
from datetime import datetime, timezone
import json
from validation import validate_and_sanitize
from email_service import send_enquiry_email

app = Flask(__name__)
ALLOWED_ORIGINS = {"http://127.0.0.1:8000", "http://localhost:8000"}

@app.after_request
def add_cors_headers(response):
    origin = request.headers.get("Origin")
    if origin in ALLOWED_ORIGINS:
        response.headers["Access-Control-Allow-Origin"] = origin
        response.headers["Vary"] = "Origin"
    response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response

@app.route("/api/enquiry", methods=["POST", "OPTIONS"])
def enquiry():
    if request.method == "OPTIONS":
        return make_response(("", 204))
    try:
        payload = request.get_json(force=True, silent=True)
    except Exception:
        return jsonify({"success": False, "error": "Invalid JSON"}), 400
    if not isinstance(payload, dict):
        return jsonify({"success": False, "error": "Invalid request body"}), 400
    ok, result = validate_and_sanitize(payload)
    if not ok:
        return jsonify({"success": False, "error": result}), 400
    clean = result.copy()
    clean["timestamp"] = datetime.now(timezone.utc).isoformat()
    try:
        send_enquiry_email(clean)
    except Exception:
        return jsonify({"success": False, "error": "Unable to send email"}), 502
    return jsonify({"success": True}), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
