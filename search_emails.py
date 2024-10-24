import logging
from utils import auth

def search_messages(service, query):
    """
    Searches for emails in the user's Gmail account based on a query string.

    Parameters:
    service (obj): The Gmail API service object.
    query (str): The search query string to filter emails (e.g., "subject:meeting" or "from:example@gmail.com").

    Returns:
    list: A list of message IDs that match the search query.
    """
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
        logging.error(f"Error occured in search_messages:{e}")


def search_email(search_text):
    """
    Searches for emails based on a specific text query.

    Parameters:
    search_text (str): The search query (e.g., "subject:report", "from:someone@example.com").

    Returns:
    None
    """
    try:
        if len(search_text) == 0:
            raise Exception("No search text given")
        # get the Gmail API service
        service = auth.gmail_authenticate() 
        search_results = search_messages(service,search_text)
        return "Nothing matched the search text" if search_results == [] else search_results
    except Exception as e:
        logging.error(f"Error occured in search_email:{e}")


