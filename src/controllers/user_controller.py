import re
from flask import jsonify, request
from db.instance import db
from models.user_model import User


class UserController:
    def create(self):
        data = request.json

        if "username" in data and "password" in data:
            user = User(
                username=data["username"],
                password=data["password"],
            )

            db.session.add(user)
            db.session.commit()
            return jsonify({"id": user.id}), 201
        return jsonify({"error": "Invalid product data"}), 400

