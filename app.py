from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__, template_folder='.')

# Serve the main page
@app.route('/')
def index():
    return render_template('index.html')

# Receive and log location data
@app.route('/log_location', methods=['POST'])
def log_location():
    data = request.json
    lat = data.get('latitude')
    lon = data.get('longitude')
    ua = data.get('user_agent', 'unknown')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    log_entry = f"{timestamp} - Lat: {lat}, Lon: {lon}, UA: {ua}\n"

    # Save to file (ephemeral on Render)
    with open('log.txt', 'a') as f:
        f.write(log_entry)

    # Also print to console (visible in Render Logs tab)
    print(log_entry.strip())

    return jsonify({'status': 'success'})

# Optional: View log.txt in browser
@app.route('/logs')
def view_logs():
    try:
        with open('log.txt', 'r') as f:
            content = f.read()
        return f"<pre>{content}</pre>"
    except FileNotFoundError:
        return "<pre>No logs yet.</pre>"

# Run locally (Render uses gunicorn instead)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
