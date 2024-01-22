from controllers.cart_items_controller import CartItemsController
from middlewares.login_required import login_required


def cart_items_routes(app):
    cart_items_controller = CartItemsController()

    @app.route("/api/cart", methods=["GET"])
    @login_required
    def get_items():
        return cart_items_controller.get()

    @app.route("/api/cart/<uuid:id>", methods=["POST"])
    @login_required
    def add_item(id):
        return cart_items_controller.add(id)

    @app.route("/api/cart/<uuid:id>", methods=["DELETE"])
    @login_required
    def delete_item(id):
        return cart_items_controller.delete(id)

    @app.route("/api/cart/checkout", methods=["POST"])
    @login_required
    def checkout_cart():
        return cart_items_controller.buy()
