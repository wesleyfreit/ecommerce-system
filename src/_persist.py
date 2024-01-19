from app import app
from db.instance import db

with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.commit()
