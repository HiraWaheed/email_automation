
import os
from utils import auth
from dotenv import load_dotenv
from base64 import urlsafe_b64decode, urlsafe_b64encode
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from mimetypes import guess_type as guess_mime_type

load_dotenv()
sender_email = os.getenv("SENDER_EMAIL")

# Adds the attachment with the given filename to the given message
def add_attachment(message, filename):
    try:
        content_type, encoding = guess_mime_type(filename)
        if content_type is None or encoding is not None:
            content_type = 'application/octet-stream'
        main_type, sub_type = content_type.split('/', 1)
        if main_type == 'text':
            fp = open(filename, 'rb')
            msg = MIMEText(fp.read().decode(), _subtype=sub_type)
            fp.close()
        elif main_type == 'image':
            fp = open(filename, 'rb')
            msg = MIMEImage(fp.read(), _subtype=sub_type)
            fp.close()
        elif main_type == 'audio':
            fp = open(filename, 'rb')
            msg = MIMEAudio(fp.read(), _subtype=sub_type)
            fp.close()
        else:
            fp = open(filename, 'rb')
            msg = MIMEBase(main_type, sub_type)
            msg.set_payload(fp.read())
            fp.close()
        filename = os.path.basename(filename)
        msg.add_header('Content-Disposition', 'attachment', filename=filename)
        message.attach(msg)
    except Exception as e:
            print(e)

def build_message(destination, obj, body, attachments=[]):
    try:
        if not attachments: # no attachments given
            message = MIMEText(body)
            message['to'] = destination
            message['from'] = sender_email
            message['subject'] = obj
        else:
            message = MIMEMultipart()
            message['to'] = destination
            message['from'] = sender_email
            message['subject'] = obj
            message.attach(MIMEText(body))
            for filename in attachments:
                add_attachment(message, filename)
        return {'raw': urlsafe_b64encode(message.as_bytes()).decode()}
    except Exception as e:
        print(e)

def send_message(service, destination, obj, body, attachments=[]):
    try:
        return service.users().messages().send(
        userId="me",
        body=build_message(destination, obj, body, attachments)
        ).execute()
    except Exception as e:
        print(e)

# get the Gmail API service
service = auth.gmail_authenticate()

receiver_email = "example@gmail.com"
send_message(service, receiver_email, "Example email subject", "Example email body")