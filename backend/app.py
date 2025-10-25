from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
]

@app.route("/api/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/api/users", methods=["POST"])
def add_user():
    data = request.json
    if not data or "name" not in data:
        return jsonify({"error": "Name required"}), 400
    new_user = {"id": len(users) + 1, "name": data["name"]}
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
