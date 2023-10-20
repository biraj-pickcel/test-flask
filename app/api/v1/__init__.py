from flask import Blueprint

from .knowledge.routes import bp as knowledge_bp
from .llm.routes import bp as llm_bp
from .webhooks.routes import bp as webhooks_bp

bp = Blueprint('v1', __name__)

bp.register_blueprint(knowledge_bp, url_prefix='/knowledge')
bp.register_blueprint(llm_bp, url_prefix='/llm')
bp.register_blueprint(webhooks_bp, url_prefix='/webhooks')