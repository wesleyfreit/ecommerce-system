from app import app
from db.instance import db

from models.user_model import User
from config.constants import USER, PASSWORD


def create_admin():
    admin = User(
        username=USER,
        password=PASSWORD,
        is_admin=True,
    )
    db.session.add(admin)


with app.app_context():
    create_admin()
    db.session.commit()
