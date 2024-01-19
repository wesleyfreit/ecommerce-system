from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user
from flask import jsonify, request

from db.instance import db
from models.user_model import User


class UserController:
    def create(self):
        data = request.json

        if "username" in data and "password" in data:
            user = User.query.filter_by(username=data["username"]).first()

            if user:
                return jsonify({"error": "User already exists"}), 400

            password_hash = generate_password_hash(data["password"])

            user = User(
                username=data["username"],
                password=password_hash,
            )

            db.session.add(user)
            db.session.commit()
            return jsonify({"info": "User created"}), 201
        return jsonify({"error": "Invalid user data"}), 400

    def login(self):
        data = request.json

        user = User.query.filter_by(username=data["username"]).first()

        if user:
            password = data.get("password")
            password_hash = user.password

            if check_password_hash(password_hash, password):
                login_user(user)
                return jsonify({"info": "User logged in"})
        return jsonify({"error": "Invalid credentials"}), 401

    def logout(self):
        logout_user()
        return jsonify({"info": "User logged out"})

    def find(self, id):
        user = User.query.get(id)
        return user
