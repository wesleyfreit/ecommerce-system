from flask import request
from db.migrations import db, Product


def product_routes(app):
    @app.route("/api/products", methods=["POST"])
    def add_product():
        data = request.json
        product = Product(
            name=data["name"],
            price=data["price"],
            description=data.get("description", ""),
        )
        db.session.add(product)
        db.session.commit()
        return "created"
