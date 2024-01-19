from functools import wraps
from flask import jsonify
from flask_login import current_user


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated and not current_user.is_admin:
            return jsonify({"error": "Forbidden action"}), 403
        return f(*args, **kwargs)

    return decorated_function
