from flask import Flask

from app.api.v1 import bp as v1_api_bp
from app.utils.db import connect_to_db


def create_app():
    connect_to_db()

    app = Flask(__name__)

    app.register_blueprint(v1_api_bp, url_prefix="/api/v1")

    @app.route("/")
    def index():
        return {"success": True, "message": "Hello World!"}

    @app.errorhandler(404)
    def not_found(e):
        return {"success": False, "message": "not found"}, 404

    return app
