from db.instance import db
from sqlalchemy import UUID
import uuid


class Product(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            **(
                {"description": self.description}
                if self.description
                else {}
            ),
        }
