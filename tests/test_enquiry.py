import unittest
from unittest.mock import MagicMock, patch
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from api.enquiry import send_email, validate, sanitize_text

class TestEnquiry(unittest.TestCase):
    def test_sanitize_text(self):
        # Normal
        self.assertEqual(sanitize_text("Hello", 10), "Hello")

        # Control chars removed
        self.assertEqual(sanitize_text("He\x00llo", 10), "Hello")

        # Truncation before filtering behavior
        # Input: "A" + 10 control chars + "B", max_len=2
        # Truncate(2) -> "A\x00", Filter -> "A"
        self.assertEqual(sanitize_text("A" + "\x00" * 10 + "B", 2), "A")

        # Long string truncation
        self.assertEqual(sanitize_text("A" * 10, 5), "AAAAA")

    def test_validate(self):
        # Valid
        ok, res = validate({"name": "John", "email": "john@example.com"})
        self.assertTrue(ok)
        self.assertEqual(res["name"], "John")

        # Invalid
        ok, res = validate({"name": "", "email": "bad"})
        self.assertFalse(ok)

    def setUp(self):
        # Reset global state before each test
        import api.enquiry
        api.enquiry._smtp_client = None

    @patch("smtplib.SMTP")
    def test_send_email(self, mock_smtp):
        mock_server = MagicMock()
        # The new implementation doesn't use context manager (with stmt),
        # so it uses mock_smtp.return_value directly, not .__enter__.return_value
        mock_smtp.return_value = mock_server

        # Also mock context manager just in case, though it shouldn't be used now
        mock_smtp.return_value.__enter__.return_value = mock_server

        data = {
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "555-0199",
            "collegeName": "My College",
            "inquiryType": "general"
        }

        send_email(data)

        # Check if SMTP was initialized
        mock_smtp.assert_called()
        # Check if timeout was passed (default 10)
        _, kwargs = mock_smtp.call_args
        self.assertEqual(kwargs.get('timeout'), 10)

        # Check if message was sent
        mock_server.send_message.assert_called_once()
        msg = mock_server.send_message.call_args[0][0]
        self.assertIn("John Doe", msg.get_content())
        self.assertEqual(msg["Subject"], "New ISM College Enquiry – CSISM Website")

    @patch("smtplib.SMTP")
    def test_send_email_reuses_connection(self, mock_smtp):
        mock_server = MagicMock()
        mock_smtp.return_value = mock_server

        data = {
            "name": "Jane Doe",
            "email": "jane@example.com",
            "phone": "555-0199",
            "collegeName": "My College",
            "inquiryType": "general"
        }

        # First call: should initialize SMTP
        send_email(data)
        self.assertEqual(mock_smtp.call_count, 1)
        self.assertEqual(mock_server.send_message.call_count, 1)

        # Second call: should reuse existing SMTP (no new init)
        send_email(data)
        self.assertEqual(mock_smtp.call_count, 1)
        self.assertEqual(mock_server.send_message.call_count, 2)

if __name__ == '__main__':
    unittest.main()
