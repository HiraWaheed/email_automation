# email_automation
This Python-based project can help you automate your emails with a single click. Utilizing google client api, you can send emails, read emails and search emails. 

# Setup
1. Set up a Google Cloud project:
- Go to the Google Cloud Console (https://console.cloud.google.com/).
- Create a new project or use an existing one.
- Enable the Gmail API for your project.
2. Set up OAuth 2.0 Credentials:
- Create OAuth 2.0 client credentials for your project.
- Select Desktop App as the Application type while creating OAuth client id
- Download the JSON file containing your client ID and client secret 
  -- Place the file in the same folder as this
  -- Replace the file's path as CREDS_FILE in the **constants.py**
3. Install required dependencies:
- `pip install -r requirements.txt`
4. Run the file:
- `python3 send_emails.py`



# Note
- When running the authentication for the first time, it will redirect to the browser for the necessary permissions.
