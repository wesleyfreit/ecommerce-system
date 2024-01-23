from app import app
from db.instance import db


with app.app_context():
    db.create_all()
    db.session.commit()
    print("Migration created successfully")
