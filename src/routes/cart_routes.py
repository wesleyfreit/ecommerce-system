from controllers.cart_controller import CartController
from flask_login import login_required


def cart_routes(app):
    cart_controller = CartController()

    @app.route("/api/cart", methods=["GET"])
    @login_required
    def get_items():
        return cart_controller.get()

    @app.route("/api/cart/<uuid:id>", methods=["POST"])
    @login_required
    def add_item(id):
        return cart_controller.add(id)

    @app.route("/api/cart/<uuid:id>", methods=["DELETE"])
    @login_required
    def delete_item(id):
        return cart_controller.delete(id)

    @app.route("/api/cart/checkout", methods=["POST"])
    @login_required
    def checkout_cart():
        return cart_controller.buy()
