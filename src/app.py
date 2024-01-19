from flask import Flask
from db.migrations import db
from config.constants import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
app.config.from_object(SQLALCHEMY_DATABASE_URI)

db.init_app(app)


if __name__ == "__main__":
    app.run(debug=True)
