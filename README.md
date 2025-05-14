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
