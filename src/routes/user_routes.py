from controllers.user_controller import UserController


def user_routes(app):
    user_controller = UserController()

    @app.route("/api/signup", methods=["POST"])
    def signup():
        return user_controller.create()

    @app.route("/api/signin", methods=["POST"])
    def signin():
        return user_controller.login()
