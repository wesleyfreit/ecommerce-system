from flask import Blueprint

from controllers.user_controller import UserController
from middlewares.login_required import login_required


api = Blueprint("user_routes", __name__)
user_controller = UserController()


@api.route("/signup", methods=["POST"])
def signup():
    return user_controller.create()


@api.route("/signin", methods=["POST"])
def signin():
    return user_controller.login()


@api.route("/signout", methods=["POST"])
@login_required
def signout():
    return user_controller.logout()


@api.route("/users/account", methods=["GET"])
@login_required
def get_user():
    return user_controller.get()
