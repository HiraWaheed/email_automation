import logging
from utils import auth
from search_emails import search_messages
from base64 import urlsafe_b64decode

def read_message(service, message):
    """
    Retrieves and prints details (To, Subject, Date, and Body) of a specific email message.

    Parameters:
    service (obj): The Gmail API service object.
    message (dict): The email message object containing the message ID.

    Returns:
    None
    """
    try:
        msg = service.users().messages().get(userId='me', id=message['id'], format='full').execute()
        payload = msg['payload']
        headers = payload.get("headers")
        parts = payload.get("parts")
        if headers:
            for header in headers:
                name = header.get("name")
                value = header.get("value")
                if name.lower() == "to":
                    print("To:", value)
                if name.lower() == "subject":
                    print("Subject:", value)
                if name.lower() == "date":
                    print("Date:", value)
        if parts:
            for part in parts: 
                mimeType = part.get("mimeType")
                body = part.get("body")
                data = body.get("data")
                if mimeType == "text/plain":
                        if data:
                            text = urlsafe_b64decode(data).decode()
                            print("Body: ",text)
    except Exception as e:
        logging.error(f"Error occured in read_message:{e}")

def read_email(search_text):
    """
    Searches for emails based on a query string and reads the details of matching emails.

    Parameters:
    search_text (str): The search query to filter emails (e.g., "subject:invoice" or "from:example@example.com").

    Returns:
    None
    """
    try:
        # get the Gmail API service
        service = auth.gmail_authenticate()
        msgs = search_messages(service,search_text)
        for msg_id in msgs:
            read_message(service,msg_id)
    except Exception as e:
        logging.error(f"Error occured in read_email:{e}")