from db.instance import db
from sqlalchemy import UUID
import uuid


class Cart(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey("user.id"), nullable=False
    )
    product_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey("product.id"), nullable=False
    )
