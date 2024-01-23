from models.user_model import User


def login_loader(login_manager, app):
    login_manager.init_app(app)
    login_manager.login_view = "api/signin"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
