from unittest.mock import MagicMock, patch
from search_emails import search_email


@patch("search_emails.auth.gmail_authenticate")
@patch("search_emails.search_messages")
def test_search_email(mock_search_message, mock_gmail_authenticate):
    # Mock the Gmail service object
    mock_service = mock_gmail_authenticate.return_value

    search_email("Search text")

    mock_search_message.assert_called_once_with(mock_service, "Search text")


@patch("search_emails.logging.error")
@patch("search_emails.search_messages")
@patch("search_emails.auth.gmail_authenticate")
def test_search_email_exception(
    mock_gmail_authenticate, mock_search_message, mock_logging_error
):
    # Mock the Gmail service object to raise an exception when send_message is called
    mock_gmail_authenticate.return_value = MagicMock()
    mock_search_message.side_effect = Exception("")

    search_email("")

    assert "Error occured in search_email" in mock_logging_error.call_args[0][0]
    assert "No search text given" in mock_logging_error.call_args[0][0]


@patch("search_emails.auth.gmail_authenticate")
@patch("search_emails.search_messages")
def test_search_email_no_match(mock_search_messages, mock_gmail_authenticate):
    mock_gmail_authenticate.return_value = MagicMock()
    mock_search_messages.return_value = []

    result = search_email("some search text")

    assert result == "Nothing matched the search text"
    mock_search_messages.assert_called_once()
