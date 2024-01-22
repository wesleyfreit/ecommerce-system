from controllers.user_controller import UserController


def login_loader(login_manager, app):
    user_controller = UserController()

    login_manager.init_app(app)
    login_manager.login_view = "api/signin"

    @login_manager.user_loader
    def load_user(user_id):
        return user_controller.find(user_id)
