# Email Automation

This Python-based project simplifies email management with a single click. Using the Google Client API, you can **send**, **read**, and **search** emails seamlessly. Perfect for automating your daily email tasks.

## Features
- **Send Emails**: Automate sending emails directly from your script.
- **Read Emails**: Fetch and read email content programmatically.
- **Search Emails**: Easily search through your inbox using custom queries.

## Setup

### 1. Set Up a Google Cloud Project
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or use an existing one.
3. Enable the **Gmail API** for your project.

### 2. Set Up OAuth 2.0 Credentials
1. Create OAuth 2.0 client credentials.
2. Select **Desktop App** as the Application type when creating the OAuth client ID.
3. Download the JSON file containing your client ID and client secret.
4. Place this file in the project directory and update the `CREDS_FILE` path in `constants.py`.

### 3. Install Dependencies
Run the following command to install the necessary packages:
```bash
pip install -r requirements.txt
```

### 4. Run the Application
Use the following command to send emails:
```bash
python3 send_emails.py
```

## Authentication Process
On the first run, you will be redirected to a browser to grant the necessary permissions to your Google account for email access.

## Example Usage

```python
from send_emails import send_email

send_email(
    subject="Hello World!",
    body="This is an automated email.",
    recipient="example@gmail.com"
)
```
