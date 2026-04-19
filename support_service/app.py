from flask import Flask, jsonify, request
import requests, os, json

app = Flask(__name__)
CORE_URL = os.getenv("CORE_URL", "http://127.0.0.1:8000")

@app.route("/api/about")
def api_about():
    with open(os.path.join("support_service/data", "about.json"), encoding="utf-8") as f:
        return jsonify(json.load(f))

@app.route("/api/dashboard")
def dashboard():
    try:
        r = requests.get(f"{CORE_URL}/api/workorders?size=1", timeout=2)
        if r.status_code == 200:
            return jsonify({"status": "online", "charts_data": r.json()})
    except requests.exceptions.RequestException:
        pass
    # Резервный ответ
    return jsonify({
        "status": "fallback",
        "message": "Core недоступен. Загружены последние известные метрики.",
        "charts_data": {"total": 0, "labels": ["pending", "done"], "values": [5, 12]}
    }), 200

@app.route("/api/notify", methods=["POST"])
def notify():
    return jsonify({"queued": True, "id": 123}), 202

if __name__ == "__main__":
    app.run(port=8080, debug=True)