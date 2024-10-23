from utils import auth
from search_emails import search_messages
from base64 import urlsafe_b64decode

def read_message(service, message):
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
        print(e)

def read_email(search_text):
    # get the Gmail API service
    service = auth.gmail_authenticate()
    msgs = search_messages(service,search_text)
    for msg_id in msgs:
        read_message(service,msg_id)