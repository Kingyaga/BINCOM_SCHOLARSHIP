from flask import Flask, request, jsonify
import datetime
import json
# Create a Flask application instance
app = Flask(__name__)

# Define a route and function
@app.route('/get_info', methods=['GET'])
def get_info():
  # Get the query parameters from the request.
  slack_name = request.args.get("slack_name")
  track = request.args.get("track")

  # Get the current day of the week.
  current_day_of_week = datetime.datetime.now().weekday()

  # Get the current UTC time.
  current_utc_time = datetime.datetime.utcnow()

  # Validate the UTC time within +/-2 hours.
  time_difference = datetime.timedelta(hours=2)
  if current_utc_time - time_difference <= current_utc_time <= current_utc_time + time_difference:
      pass
  else:
      return "The UTC time is not within +/-2 hours."

  # Get the track name.
  if track is None:
    track = "Unknown"

  # Get the GitHub URL of the file being run.
  file_github_url = "https://github.com/<username>/<repo>/blob/<branch>/<file>"

  # Get the GitHub URL of the full source code.
  full_source_code_github_url = "https://github.com/<username>/<repo>"

  # Create a JSON object that contains the information you need to return.
  info = {
    "slack_name": slack_name,
    "current_day": current_day_of_week,
    "utc_time": current_utc_time,
    "track": track,
    "github_file_url": file_github_url,
    "github_repo_url": full_source_code_github_url
  }

  # Return the JSON object with the status code 200.
  return jsonify(info, status_code=200)

# Run the application
if __name__ == '__main__':
    app.run()