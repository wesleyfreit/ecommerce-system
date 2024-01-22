from functools import wraps
from flask import jsonify
from flask_login import current_user


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return jsonify({"error": "Unauthorized, user not logged in"}), 401
        return f(*args, **kwargs)

    return decorated_function
