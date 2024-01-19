from flask import jsonify, request
from db.instance import db
from models.user_model import User
from flask_login import login_user


class UserController:
    def create(self):
        data = request.json

        if "username" in data and "password" in data:
            user = User.query.filter_by(username=data["username"]).first()

            if user:
                return jsonify({"error": "User already exists"}), 400

            user = User(
                username=data["username"],
                password=data["password"],
            )

            db.session.add(user)
            db.session.commit()
            return jsonify({"info": "User created"}), 201
        return jsonify({"error": "Invalid user data"}), 400

    def login(self):
        data = request.json

        user = User.query.filter_by(username=data["username"]).first()

        if user:
            if data.get("password") == user.password:
                login_user(user)
                return jsonify({"info": "User logged in"})
        return jsonify({"error": "Invalid credentials"}), 401

    def find(self, id):
        user = User.query.get(id)
        return user
