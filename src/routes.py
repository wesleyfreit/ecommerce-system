from flask import request, jsonify
from db.migrations import db, Product


def product_routes(app):
    @app.route("/api/products", methods=["POST"])
    def add_product():
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

    @app.route("/api/products/<uuid:id>", methods=["GET"])
    def get_product(id):
        product = Product.query.get(id)

        if product:
            return jsonify({
                "id": product.id,
                "name": product.name,
                "price": product.price,
                "description": product.description,
            })
        return jsonify({"error": "Product not found"}), 404

    @app.route("/api/products/<uuid:id>", methods=["PUT"])
    def update_product(id):
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

    @app.route("/api/products/<uuid:id>", methods=["DELETE"])
    def delete_product(id):
        product = Product.query.get(id)

        if product:
            db.session.delete(product)
            db.session.commit()
            return jsonify(), 204
        return jsonify({"error": "Product not found"}), 404
