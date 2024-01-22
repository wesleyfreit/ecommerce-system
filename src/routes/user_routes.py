from controllers.user_controller import UserController
from middlewares.login_required import login_required


def user_routes(app):
    user_controller = UserController()

    @app.route("/api/signup", methods=["POST"])
    def signup():
        return user_controller.create()

    @app.route("/api/signin", methods=["POST"])
    def signin():
        return user_controller.login()

    @app.route("/api/signout", methods=["POST"])
    @login_required
    def signout():
        return user_controller.logout()

    @app.route("/api/users/account", methods=["GET"])
    @login_required
    def purchased_items():
        return user_controller.get()
