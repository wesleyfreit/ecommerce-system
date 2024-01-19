from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UUID
import uuid


db = SQLAlchemy()


class Product(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)
