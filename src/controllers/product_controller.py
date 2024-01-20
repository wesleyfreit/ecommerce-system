from flask import jsonify, request
from db.instance import db
from models.product_model import Product


class ProductController:
    def get(self):
        products = [product.serialize() for product in Product.query.all()]

        if products:
            return jsonify({"products": products})
        return jsonify({"products": []})

    def add(self):
        data = request.json

        if "name" in data and "price" in data:
            product = Product(
                name=data["name"],
                price=data["price"],
                description=data.get("description", ""),
            )

            db.session.add(product)
            db.session.commit()
            return jsonify({"id": product.id}), 201
        return jsonify({"error": "Invalid product data"}), 400

    def find(self, id):
        product = Product.query.get(id).serialize()

        if product:
            return jsonify({"product": product})
        return jsonify({"error": "Product not found"}), 404

    def update(self, id):
        product = Product.query.get(id)

        if not product:
            return jsonify({"error": "Product not found"}), 404

        data = request.json
        if "name" in data:
            product.name = data["name"]

        if "price" in data:
            product.price = data["price"]

        if "description" in data:
            product.description = data["description"]

        db.session.commit()

        return jsonify(), 204

    def delete(self, id):
        product = Product.query.get(id)

        if product:
            db.session.delete(product)
            db.session.commit()
            return jsonify(), 204
        return jsonify({"error": "Product not found"}), 404
