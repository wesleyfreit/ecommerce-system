from controllers.product_controller import ProductController
from flask_login import login_required

from middlewares.admin_required import admin_required


def product_routes(app):
    product_controller = ProductController()

    @app.route("/api/products", methods=["GET"])
    def get_products():
        return product_controller.get()

    @app.route("/api/products/<uuid:id>", methods=["GET"])
    def get_product(id):
        return product_controller.find(id)

    @app.route("/api/products", methods=["POST"])
    @login_required
    @admin_required
    def add_product():
        return product_controller.add()

    @app.route("/api/products/<uuid:id>", methods=["PUT"])
    @login_required
    @admin_required
    def update_product(id):
        return product_controller.update(id)

    @app.route("/api/products/<uuid:id>", methods=["DELETE"])
    @login_required
    @admin_required
    def delete_product(id):
        return product_controller.delete(id)
