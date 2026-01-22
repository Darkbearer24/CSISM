import time
import json
import sys
import os
from unittest.mock import MagicMock, patch
from io import BytesIO

# Add repo root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api import enquiry
from api.enquiry import handler

def benchmark_handler():
    print("=== Benchmarking handler.do_POST with Connection Reuse ===")

    # Reset global state
    enquiry._smtp_client = None

    payload = {
        "name": "Test User",
        "email": "test@example.com",
        "phone": "1234567890",
        "collegeName": "Test College",
        "inquiryType": "general"
    }
    body = json.dumps(payload).encode('utf-8')

    with patch("smtplib.SMTP") as mock_smtp_cls:
        mock_instance = MagicMock()

        # Simulate slow connection (2.0s)
        def delayed_connect(*args, **kwargs):
            time.sleep(2.0)
            return mock_instance

        mock_smtp_cls.side_effect = delayed_connect

        # Simulate fast send (0.1s)
        mock_instance.send_message.side_effect = lambda *args: time.sleep(0.1)

        # Simulate fast noop (check connection)
        mock_instance.noop.return_value = (250, b'Ok')

        # Run 1: Cold Start
        h1 = handler.__new__(handler)
        h1.rfile = BytesIO(body)
        h1.wfile = BytesIO()
        h1.headers = {"Content-Length": str(len(body))}
        h1.send_response = MagicMock()
        h1.send_header = MagicMock()
        h1.end_headers = MagicMock()

        print("Run 1 (Cold Start)...")
        start_time = time.time()
        h1.do_POST()
        end_time = time.time()
        t1 = end_time - start_time
        print(f"Run 1 Time: {t1:.4f} seconds")

        # Run 2: Warm Start (Reuse)
        h2 = handler.__new__(handler)
        h2.rfile = BytesIO(body)
        h2.wfile = BytesIO()
        h2.headers = {"Content-Length": str(len(body))}
        h2.send_response = MagicMock()
        h2.send_header = MagicMock()
        h2.end_headers = MagicMock()

        print("Run 2 (Warm Start)...")
        start_time = time.time()
        h2.do_POST()
        end_time = time.time()
        t2 = end_time - start_time
        print(f"Run 2 Time: {t2:.4f} seconds")

        if t2 < t1:
            print(f"Improvement: {t1 - t2:.4f} seconds saved")
        else:
            print("No improvement (something is wrong)")

if __name__ == "__main__":
    benchmark_handler()
