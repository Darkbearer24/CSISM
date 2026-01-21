import time
import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# Add repo root to path so we can import api.enquiry
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api.enquiry import send_email, sanitize_text

def benchmark():
    print("=== Benchmarking send_email ===")

    # Mock data
    data = {
        "name": "Test User",
        "email": "test@example.com",
        "phone": "1234567890",
        "collegeName": "Test College",
        "inquiryType": "general"
    }

    # Scenario 1: Fast SMTP (simulated 0.1s delay)
    with patch("smtplib.SMTP") as mock_smtp:
        mock_server = MagicMock()
        mock_smtp.return_value.__enter__.return_value = mock_server

        # Simulate network delay in send_message
        def delayed_send(*args, **kwargs):
            time.sleep(0.1)

        mock_server.send_message.side_effect = delayed_send

        start_time = time.time()
        send_email(data)
        end_time = time.time()

        print(f"Scenario 1 (Fast SMTP 0.1s): {end_time - start_time:.4f} seconds")

    # Scenario 2: Slow SMTP (simulated 2.0s delay)
    with patch("smtplib.SMTP") as mock_smtp:
        mock_server = MagicMock()
        mock_smtp.return_value.__enter__.return_value = mock_server

        def delayed_send(*args, **kwargs):
            time.sleep(2.0)

        mock_server.send_message.side_effect = delayed_send

        start_time = time.time()
        send_email(data)
        end_time = time.time()

        print(f"Scenario 2 (Slow SMTP 2.0s): {end_time - start_time:.4f} seconds")

    print("\n=== Benchmarking sanitize_text ===")
    long_string = "a" * 1000 + "\t\n" + "b" * 1000 + "".join(chr(i) for i in range(32))
    iterations = 100000

    start_time = time.time()
    for _ in range(iterations):
        sanitize_text(long_string)
    end_time = time.time()
    print(f"sanitize_text (100k iters): {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    benchmark()
