from flask import Flask, request, jsonify, render_template
from datetime import datetime
import os

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

    # Ensure log.txt exists or append to it
    with open('log.txt', 'a') as f:
        f.write(f"{timestamp} - Lat: {lat}, Lon: {lon}\n")

    return jsonify({'status': 'success'})

# For local development only
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
