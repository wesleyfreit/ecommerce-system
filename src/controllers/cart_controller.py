from flask import jsonify
from flask_login import current_user

from db.instance import db
from models.cart_model import Cart
from models.product_model import Product
from models.user_model import User


class CartController:
    def get(self):
        user = User.query.get(current_user.id)
        cart_items = user.cart

        if cart_items:
            items = [
                Product.query.get(
                    item.product_id
                ).serialize() for item in cart_items
            ]
            return jsonify({"cart_items": items})
        return jsonify({"cart_items": []})

    def add(self, id):
        user_id = current_user.id
        product = Product.query.get(id)

        if product:
            cart_item = Cart(user_id=user_id, product_id=product.id)

            db.session.add(cart_item)
            db.session.commit()

            return jsonify({"info": "Item added to cart"}), 201
        return jsonify({"error": "Item not found"}), 404

    def delete(self, id):
        user_id = current_user.id
        cart_item = Cart.query.filter_by(
            user_id=user_id, product_id=id
        ).first()

        if cart_item:
            db.session.delete(cart_item)
            db.session.commit()

            return jsonify({"info": "Item removed from cart"}), 200
        return jsonify({"error": "Item not found"}), 404

    def buy(self):
        return "buy items"
