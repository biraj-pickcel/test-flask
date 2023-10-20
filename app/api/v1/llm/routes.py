from flask import Blueprint

from . import controllers

bp = Blueprint("llm", __name__)


@bp.route("/ask", methods=["POST"])
def ask():
    return controllers.ask()
