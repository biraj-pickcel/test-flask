from flask import Blueprint

from . import controllers

bp = Blueprint("knowledge", __name__)


@bp.route("/crawl", methods=["POST"])
def crawl():
    return controllers.crawl()
