from db.instance import db
from sqlalchemy import UUID
from datetime import datetime
import uuid


class UserProducts(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey("user.id"), nullable=False
    )
    product_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey("product.id"), nullable=False
    )
    purchase_date = db.Column(
        db.DateTime, nullable=False, default=datetime.now()
    )
