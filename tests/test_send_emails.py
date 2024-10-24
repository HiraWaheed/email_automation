from unittest.mock import MagicMock, patch
from send_emails import send_email


@patch("send_emails.auth.gmail_authenticate")
@patch("send_emails.send_message")
def test_send_email(mock_send_message, mock_gmail_authenticate):
    # Mock the Gmail service object
    mock_service = mock_gmail_authenticate.return_value

    send_email("test@example.com", "Test Subject", "Test Body")

    mock_send_message.assert_called_once_with(
        mock_service, "test@example.com", "Test Subject", "Test Body"
    )


@patch("send_emails.logging.error")
@patch("send_emails.send_message")
@patch("send_emails.auth.gmail_authenticate")
def test_send_email_exception(
    mock_gmail_authenticate, mock_send_message, mock_logging_error
):
    # Mock the Gmail service object to raise an exception when send_message is called
    mock_gmail_authenticate.return_value = MagicMock()
    mock_send_message.side_effect = Exception("To header invalid")

    send_email("", "Test Subject", "Test Body")

    assert "Error occured in send_email" in mock_logging_error.call_args[0][0]
    assert "To header invalid" in mock_logging_error.call_args[0][0]
