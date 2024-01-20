from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager

from db.instance import db
from config.constants import DATABASE_URL, SECRET_KEY

from middlewares.login_required import login_required
from routes.cart_items_routes import cart_items_routes
from routes.product_routes import product_routes
from routes.user_routes import user_routes

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

login_manager = LoginManager()

db.init_app(app)

login_required(login_manager, app)

CORS(app)

product_routes(app)
user_routes(app)
cart_items_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
