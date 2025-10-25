from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains (important for Vue)
api = Api(app)

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
]

class UserList(Resource):
    def get(self):
        return users

    def post(self):
        data = request.get_json()
        new_user = {"id": len(users) + 1, "name": data["name"]}
        users.append(new_user)
        return new_user, 201

api.add_resource(UserList, "/api/users")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
