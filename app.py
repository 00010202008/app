from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/log_location', methods=['POST'])
def log_location():
    data = request.json
    lat = data.get('latitude')
    lon = data.get('longitude')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    log_entry = f"{timestamp} - Lat: {lat}, Lon: {lon}\n"

    # Write to file (ephemeral on Render)
    with open('log.txt', 'a') as f:
        f.write(log_entry)

    # Print to console (visible in Render logs)
    print(log_entry.strip())

    return jsonify({'status': 'success'})

# OPTIONAL: View logs in browser
@app.route('/logs')
def view_logs():
    try:
        with open('log.txt', 'r') as f:
            content = f.read()
        return f"<pre>{content}</pre>"
    except FileNotFoundError:
        return "<pre>No logs yet.</pre>"

# For local development only (Render uses gunicorn)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
