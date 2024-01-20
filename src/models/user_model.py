from datetime import datetime
from db.instance import db
from flask_login import UserMixin
from sqlalchemy import UUID
import uuid


class User(db.Model, UserMixin):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    items_purchased = db.relationship(
        "UserProducts", backref="user", lazy=True
    )
    cart_items = db.relationship("CartItems", backref="user", lazy=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
