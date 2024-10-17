# Python Keylogger with Google Drive Integration

A simple Python keylogger that captures keystrokes and uploads logs to Google Drive.

## Features
- Captures keystrokes
- Uploads logs to a specified Google Drive folder

## Requirements
- Python 3.x
- `pynput` library
- Google Drive API credentials (service account)

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Python-Keylogger-Google-Drive.git
   ```
2. Install the required libraries:
   ```bash
   pip install pynput google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
   ```
3. Set up Google Drive API and create a service account. Download the JSON credentials file and update the `SERVICE_ACCOUNT_FILE` path in the script.
4. Enter the Google Drive folder ID where you want to upload the logs.
5. Run the script:
   ```bash
   python your_script_name.py
   ```

## Important Note
This script is intended for educational purposes only. Use responsibly and ensure compliance with applicable laws and regulations.
