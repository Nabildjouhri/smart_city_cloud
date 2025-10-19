from flask import Flask, request, jsonify
from flask_cors import CORS
import random, time

app = Flask(__name__)
CORS(app)

users = []
sensor_data = []

@app.route('/')
def home():
    return jsonify({"message": "Smart City Cloud API is running!"})

@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    user = {
        "name": data.get("name"),
        "surname": data.get("surname"),
        "zone": data.get("zone")
    }
    users.append(user)
    return jsonify({"status": "registered", "user": user})

@app.route('/send_data', methods=['POST'])
def send_data():
    data = request.get_json()
    data["timestamp"] = time.time()
    sensor_data.append(data)
    return jsonify({"status": "received", "data": data})

@app.route('/latest_data', methods=['GET'])
def latest_data():
    if not sensor_data:
        return jsonify({"error": "No data yet"})
    return jsonify(sensor_data[-1])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
