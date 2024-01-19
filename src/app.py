from flask import Flask
from db.migrations import db
from config.constants import DATABASE_URL
import routes

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

db.init_app(app)

routes.product_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
