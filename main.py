import datetime as dt
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/calendar"]

def main():
    creds = None

    if os.path.exists("token.json"):
        try:
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        except Exception as e:
            print(f"Error loading credentials from file: {e}")

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception as e:
                print(f"Error refreshing credentials: {e}")
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials-web.json", SCOPES)
            creds = flow.run_local_server(port=0)
        
        if creds:
            with open("token.json", "w") as token:
                token.write(creds.to_json())
        else:
            print("Failed to obtain credentials")
            return

    try:
        service = build('calendar', 'v3', credentials=creds)
        now = dt.datetime.now().isoformat() + "Z"
        event_result = service.events().list(calendarId="primary", 
            timeMin=now, maxResults=10, singleEvents=True, 
            orderBy="startTime").execute()
        events = event_result.get("items", [])

        if not events:
            print("No events")
            return
        
        for event in events:
            start = event["start"].get("dateTime", 
                    event["start"].get("date"))
            print(start, event["summary"])
            print(event)

    except HttpError as e:
        print("Error occurred:", e)

if __name__ == "__main__":
    main()