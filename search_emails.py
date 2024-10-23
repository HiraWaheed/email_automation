from utils import auth

def search_messages(service, query):
    try:
        result = service.users().messages().list(userId='me',q=query).execute()
        messages = [ ]
        if 'messages' in result:
            messages.extend(result['messages'])
        while 'nextPageToken' in result:
            page_token = result['nextPageToken']
            result = service.users().messages().list(userId='me',q=query, pageToken=page_token).execute()
            if 'messages' in result:
                messages.extend(result['messages'])
        return messages
    except Exception as e:
        print(e)


def search_email(search_text):
    # get the Gmail API service
    service = auth.gmail_authenticate()
    search_messages(service,search_text)


