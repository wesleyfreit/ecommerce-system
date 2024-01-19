from werkzeug.security import generate_password_hash
from app import app
from db.instance import db

from models.user_model import User
from config.constants import USER, PASSWORD


def create_admin():
    password_hash = generate_password_hash(PASSWORD)
    admin = User(
        username=USER,
        password=password_hash,
        is_admin=True,
    )
    db.session.add(admin)


with app.app_context():
    create_admin()
    db.session.commit()
