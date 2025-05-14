from flask import Flask, render_template, request, redirect
import plotly.express as px
import pandas as pd

# custom python modules
from vibes import vibes
from vibes import config


app = Flask(__name__)

# Initialize Google Sheets helper
gs_logger = vibes.GoogleSheetsLogger(
    credentials_file=config.GOOGLE_SHEETS_CREDENTIALS_FILE,
    sheet_name=config.GOOGLE_SHEETS_NAME)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        patient_mood = request.form.get("mood")
        # redirect if mood is default value of "Select..."
        if patient_mood == config.DEFAULT_MOOD:
            error_msg = "Please select a valid mood."
            return render_template(
                template_name_or_list="index.html",
                defaultMood=config.DEFAULT_MOOD,
                moodsList=config.MOODS_LIST,
                errorMsg=error_msg
            )
        note = request.form.get("note")
        gs_logger.log_mood(mood=patient_mood, note=note)

        # submission was successful - redirect to complete or finish page
        return redirect("/complete")

    return render_template(
        template_name_or_list="index.html",
        defaultMood=config.DEFAULT_MOOD,
        moodsList=config.MOODS_LIST
    )


@app.route("/complete")
def complete():
    return render_template("complete.html")


@app.route("/charts")
def charts():
    data = gs_logger.get_all_records()
    df = pd.DataFrame(data)

    # TODO: move this logic to vibes.py
    # Create barchart summary
    if "Timestamp" in df.columns:
        df["Timestamp"] = pd.to_datetime(df["Timestamp"])
        df["Date"] = df["Timestamp"].dt.date

    mood_counts = df.groupby(["Date", "Emotion"]).size().reset_index(name="Count")
    fig = px.bar(mood_counts, x="Date", y="Count", color="Emotion", title="Mood Frequency by Day")
    plotly_chart_html = fig.to_html(full_html=False)

    return render_template(
        template_name_or_list="charts.html",
        plotly_chart=plotly_chart_html
    )


if __name__ == "__main__":
    app.run(debug=False)
