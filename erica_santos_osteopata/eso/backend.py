from __future__ import print_function
import os.path
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def insert_calendar_event(summary, description, start_datetime, end_datetime):
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('staticfiles/token.json'):
        creds = Credentials.from_authorized_user_file('staticfiles/token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'staticfiles/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('staticfiles/token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    event_info = {
        'summary': summary,
        'description': description,
        'start': {
        'dateTime': f'{start_datetime.year}-{start_datetime.month}-{start_datetime.day}T{start_datetime.hour-1}:{start_datetime.minute}:00-00:00',
        'timeZone': 'America/Los_Angeles',
        },
        'end': {
        'dateTime': f'{end_datetime.year}-{end_datetime.month}-{end_datetime.day}T{end_datetime.hour-1}:{end_datetime.minute}:00-00:00',
        'timeZone': 'America/Los_Angeles',
        },
        'recurrence': [
        'RRULE:FREQ=DAILY;COUNT=1'
        ],
        'attendees': [
        {'email': 'jmoutinho94@gmail.com'}
        ],
        'reminders': {
        'useDefault': False,
        'overrides': [
          {'method': 'email', 'minutes': 24 * 60},
          {'method': 'popup', 'minutes': 10},
        ],
        },
        }

    event = service.events().insert(calendarId='primary', body=event_info).execute()



