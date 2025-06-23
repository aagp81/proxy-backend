from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Para permitir peticiones desde tu frontend en Vercel

API_URL = "http://47.99.135.189:8080/wx/auth/login"

@app.route("/auth/login", methods=["POST"])
def proxy_login():
    data = request.get_json()
    try:
        response = requests.post(API_URL, json=data)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": "No se pudo contactar con la API", "details": str(e)}), 500

if __name__ == "__main__":
    app.run()
