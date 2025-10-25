from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow requests from Vue frontend
api = Api(app)

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

class UserList(Resource):
    def get(self):
        return {"users": users}, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", required=True)
        args = parser.parse_args()
        new_user = {"id": len(users) + 1, "name": args["name"]}
        users.append(new_user)
        return new_user, 201

api.add_resource(UserList, "/api/users")

if __name__ == "__main__":
    app.run(debug=True)
