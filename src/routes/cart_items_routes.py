from flask import Blueprint

from controllers.cart_items_controller import CartItemsController
from middlewares.login_required import login_required


api = Blueprint("cart_items_routes", __name__)
cart_items_controller = CartItemsController()


@api.route("/cart", methods=["GET"])
@login_required
def get_items():
    return cart_items_controller.get()


@api.route("/cart/<uuid:id>", methods=["POST"])
@login_required
def add_item(id):
    return cart_items_controller.add(id)


@api.route("/cart/<uuid:id>", methods=["DELETE"])
@login_required
def delete_item(id):
    return cart_items_controller.delete(id)


@api.route("/cart/checkout", methods=["POST"])
@login_required
def checkout_cart():
    return cart_items_controller.buy()


@api.route("/cart/clean", methods=["DELETE"])
@login_required
def clean_cart():
    return cart_items_controller.clean()
