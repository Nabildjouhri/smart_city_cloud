from flask import Flask, jsonify, request
import random
import time

app = Flask(__name__)

# قائمة المناطق (يمكن تعديلها لاحقًا)
ZONES = ["Centre", "Nord", "Sud", "Est", "Ouest"]

def generate_zone_data():
    """رجّع بيانات عشوائية لكل منطقة"""
    data = {}
    for zone in ZONES:
        data[zone] = {
            "waste": random.randint(0, 100),   # نسبة امتلاء سلة النفايات
            "light": random.randint(0, 100),   # شدة الإضاءة
            "air": random.randint(0, 500),     # جودة الهواء (ppm أو مؤشر)
            "timestamp": int(time.time())
        }
    return data

@app.route('/')
def home():
    return jsonify({"message": "Smart City Cloud API is running!"})

@app.route('/data', methods=['GET'])
def get_all_data():
    """إرجاع بيانات كل المناطق"""
    return jsonify(generate_zone_data())

@app.route('/data/<zone>', methods=['GET'])
def get_zone_data(zone):
    """إرجاع بيانات منطقة معينة (case-insensitive)"""
    zone_normal = zone.capitalize()
    if zone_normal not in ZONES:
        return jsonify({"error": "Zone not found", "available_zones": ZONES}), 404

    return jsonify({
        "zone": zone_normal,
        "waste": random.randint(0, 100),
        "light": random.randint(0, 100),
        "air": random.randint(0, 500),
        "timestamp": int(time.time())
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
