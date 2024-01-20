from flask import jsonify
from flask_login import current_user

from db.instance import db
from models.cart_items_model import CartItems
from models.user_products_model import UserProducts
from models.product_model import Product
from models.user_model import User


class CartItemsController:
    def get(self):
        user = User.query.get(current_user.id)
        cart_items = [item.product_id for item in user.cart_items]

        if cart_items:
            products = Product.query.all()

            items = [
                product.serialize()
                for product in products
                if product.id in cart_items
            ]

            return jsonify({"cart_items": items})
        return jsonify({"cart_items": []})

    def add(self, id):
        user_id = current_user.id
        product = Product.query.get(id)

        if product:
            cart_item = CartItems(user_id=user_id, product_id=product.id)

            db.session.add(cart_item)
            db.session.commit()

            return jsonify({"info": "Item added to cart"}), 201
        return jsonify({"error": "Item not found"}), 404

    def delete(self, id):
        user_id = current_user.id
        cart_item = CartItems.query.filter_by(
            user_id=user_id,
            product_id=id
        ).first()

        if cart_item:
            db.session.delete(cart_item)
            db.session.commit()

            return jsonify({"info": "Item removed from cart"}), 200
        return jsonify({"error": "Item not found"}), 404

    def buy(self):
        user = User.query.get(current_user.id)
        cart_items = user.cart_items

        for item in cart_items:
            purchase_product = UserProducts(
                user_id=item.user_id,
                product_id=item.product_id
            )
            db.session.add(purchase_product)
            db.session.delete(item)
        db.session.commit()

        return jsonify({"info": "Cart purchased successfully"})
