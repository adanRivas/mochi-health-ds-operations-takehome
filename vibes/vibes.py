import configparser
import datetime

import gspread
from google.oauth2.service_account import Credentials


# read in config.ini
config = configparser.ConfigParser()
config.read("config.ini")
GOOGLE_SHEETS_ID = config["GOOGLE"]["SHEETS_ID"]


class GoogleSheetsLogger:
    def __init__(self, credentials_file, sheet_name):
        scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        gcp_creds = Credentials.from_service_account_file(credentials_file, scopes=scopes)
        self.client = gspread.authorize(gcp_creds)
        self.workbook = self.client.open_by_key(GOOGLE_SHEETS_ID)
        # TODO: add logic to verify sheet name exits first, else throw an error
        self.sheet = self.workbook.worksheet(sheet_name)

    def log_mood(self, mood, note):
        """
        Logs mood along with (optional) note and timestamp to Google Sheets.
        """
        # do not directly log an empty string into the spreadsheet
        # this could complicate post hoc analysis
        if note == '':
            note = None

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.sheet.append_row([mood, note, timestamp])

    def get_all_records(self):
        """
        Get all logged vibes from Google Sheet tracker.
        """
        return self.sheet.get_all_records()
