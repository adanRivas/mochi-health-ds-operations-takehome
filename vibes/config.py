import os
import json
import tempfile


# List of predefined emotions
MOODS_LIST = ["Happy", "Down", "Excited", "Nervous", "Anxious", "Relaxed", "Grateful", "Upset", "Mad", "Other"]
DEFAULT_MOOD = 'Choose...'

# Google Sheets configuration
GOOGLE_SHEETS_WORKBOOK_NAME = 'Mochi Patient Vibes'
GOOGLE_SHEETS_NAME = "vibes"
GOOGLE_SHEETS_CREDENTIALS_FILE = "mochi-vibes-credentials.json"


# Try to get the JSON credentials from the environment if app is deployed
credentials_json_str = os.environ.get("GOOGLE_SHEETS_CREDENTIALS")

if credentials_json_str:
    # # Option 1: Work with the credentials directly as a dictionary
    # GOOGLE_SHEETS_CREDENTIALS = json.loads(credentials_json_str)

    # Option 2: Create a temporary file for libraries that require a file
    # Uncomment the following block if a file is needed.

    with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.json') as temp_cred_file:
        temp_cred_file.write(credentials_json_str)
        GOOGLE_SHEETS_CREDENTIALS_FILE = temp_cred_file.name
