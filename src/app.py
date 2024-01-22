from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager

from db.instance import db
from config.constants import DATABASE_URL, SECRET_KEY

from middlewares.login_loader import login_loader
from routes.cart_items_routes import api as cart_items_routes
from routes.product_routes import api as product_routes
from routes.user_routes import api as user_routes

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

login_manager = LoginManager()

db.init_app(app)

login_loader(login_manager, app)

CORS(app)

app.register_blueprint(cart_items_routes, url_prefix="/api")
app.register_blueprint(product_routes, url_prefix="/api")
app.register_blueprint(user_routes, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
