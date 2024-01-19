from flask import Flask
from db.instance import db
from config.constants import DATABASE_URL
from routes.product_routes import product_routes

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

db.init_app(app)

product_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
