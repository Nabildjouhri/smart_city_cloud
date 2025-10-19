from flask import Flask, jsonify
import random
import time
import os

app = Flask(__name__)

# قائمة المناطق (Zones)
ZONES = ["Centre", "Nord", "Sud"]

# دالة توليد بيانات عشوائية لمحاكاة القبطورات
def generate_zone_data():
    data = {}
    for zone in ZONES:
        data[zone] = {
            "waste": random.randint(0, 100),
            "light": random.randint(0, 100),
            "air": random.randint(0, 100),
            "timestamp": int(time.time())
        }
    return data

# الصفحة الرئيسية (اختبار فقط)
@app.route('/')
def home():
    return jsonify({"message": "Smart City Cloud API is running!"})

# المسار الذي يعرض بيانات كل المناطق
@app.route('/data', methods=['GET'])
def get_all_data():
    return jsonify(generate_zone_data())

# المسار الذي يعرض بيانات منطقة واحدة فقط
@app.route('/data/<zone>', methods=['GET'])
def get_zone_data(zone):
    zone_cap = zone.capitalize()
    if zone_cap not in ZONES:
        return jsonify({"error": "Zone not found", "available_zones": ZONES}), 404
    return jsonify({zone_cap: generate_zone_data()[zone_cap]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
