from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

TARGET_API = "http://47.99.135.189:8080/wx"

@app.route('/api/<path:path>', methods=['GET', 'POST'])
def proxy(path):
    url = f"{TARGET_API}/{path}"
    method = request.method

    try:
        if method == 'POST':
            response = requests.post(url, json=request.get_json(), headers={'Content-Type': 'application/json'})
        else:
            response = requests.get(url, params=request.args)

        return (response.text, response.status_code, {'Content-Type': response.headers.get('Content-Type', 'application/json')})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
