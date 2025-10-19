from flask import Flask, jsonify
import random, time

app = Flask(__name__)

# 🧠 مناطق المدينة
ZONES = ["Centre", "Nord", "Sud"]

@app.route('/')
def home():
    return jsonify({"message": "Smart City Cloud API is running!"})

# 🔁 دالة لتوليد بيانات عشوائية لكل منطقة
def generate_zone_data(zone):
    return {
        "zone": zone,
        "waste": random.randint(10, 100),   # مستوى النفايات
        "light": random.randint(50, 100),   # مستوى الإضاءة
        "air": random.randint(60, 100),     # جودة الهواء
        "timestamp": int(time.time())       # الوقت الحالي
    }

# 🌍 مسار لإرجاع كل البيانات
@app.route('/data', methods=['GET'])
def get_all_data():
    result = {zone: generate_zone_data(zone) for zone in ZONES}
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
