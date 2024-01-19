from flask import Flask
from flask_cors import CORS

from db.instance import db
from config.constants import DATABASE_URL

from routes.product_routes import product_routes
from routes.user_routes import user_routes

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

db.init_app(app)

CORS(app)

product_routes(app)
user_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
