# Mochi Health Patient Vibes: Mood Logging and Summary

## Overview

Vibes is a lightweight Flask web application that enables patients to log their mood along with an optional note. Each submission is recorded in a Google Sheets document using a custom Python module for Google Sheets integration. In addition, the app provides data visualization through interactive charts (using Plotly) that summarize mood trends over time.

## Features

- **Mood Logging:**  
  Patients can select a mood from a dropdown list or enter a custom value, and add a personal note.

- **Google Sheets Entry:**  
  Submissions are uploaded and timestamped to a private Google Sheets.

- **Submission Confirmation:**  
  After a successful mood submission, patients are redirected to a confirmation page notifying them that their entry was received.

- **Mood Visualization:**  
  An interactive charts page summarizes mood counts by day, displaying a bar chart generated with Plotly. To access, go to `charts` page.


## App Configurations

Edit the configuration file (i.e., vibes/config.py) to set:

    GOOGLE_SHEETS_CREDENTIALS_FILE: Path to your Google credentials JSON file.
    
    GOOGLE_SHEETS_NAME: Name of the Google Sheets file where moods will be recorded.
    
    DEFAULT_MOOD and MOODS_LIST: The default mood placeholder and the list of accepted mood options.


## Usage

1. Submit a Mood Entry:

- Visit https://mochi-health-ds-operations-takehome-production.up.railway.app/ in your web browser.

- Select your mood (or enter a custom one) and add any notes.

- Submit the form. If the mood is valid, you'll be redirected to a confirmation page. 

2. View Charts:

Navigate to https://mochi-health-ds-operations-takehome-production.up.railway.app/charts to see an interactive Plotly bar chart summarizing mood frequency by day.


## Near-term Enhancements

As this app graduates from a quick prototype to a more developed early product, the following TODOs remain: 

- Refactor Chart Logic: Move the Plotly and data aggregation logic from the /charts route into `vibes/vibes.py`.

- Additional Chart Filtering: Enhance the charts page with filtering options, such as by date range or specific moods, to allow for more dynamic data exploration.

- UI/UX Improvements: Improve the front-end design with a responsive layout and additional CSS templates and js frameworks (to be stored under `templates`).

