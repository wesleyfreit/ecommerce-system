from app import app
from db.migrations import db

with app.app_context():
    db.create_all()
    db.session.commit()
