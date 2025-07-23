from flask import Flask, request, jsonify
from flask_cors import CORS
import jwt
import datetime

app = Flask(__name__)
CORS(app)

SECRET_KEY = "super_secret_key"

users = {
    "admin@example.com": {"password": "123456", "role": "admin"},
    "user@example.com": {"password": "userpass", "role": "user"}
}

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    if email in users and users[email]["password"] == password:
        token = jwt.encode({
            "email": email,
            "role": users[email]["role"],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
        }, SECRET_KEY, algorithm="HS256")
        return jsonify({"token": token, "message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True)
