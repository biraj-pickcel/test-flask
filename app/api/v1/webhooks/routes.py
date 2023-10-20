from flask import Blueprint

from . import controllers

bp = Blueprint("webhooks", __name__)


@bp.route("/apify")
def apify():
    return controllers.apify()
