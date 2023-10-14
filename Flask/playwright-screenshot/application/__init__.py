"""Main Flask Application"""

from flask import Flask
from flask_cors import CORS
from flask_mailman import Mail
from flask_restful import Api

restful_api = Api()
cors = CORS()
mail = Mail()


def init_app():
    """Initialises the flask application necessary for starting the service"""

    app = Flask(__name__)
    app.config.from_object("config.Config")

    with app.app_context():
        from .api import snap_bp

        app.register_blueprint(snap_bp, url_prefix="/api")

        restful_api.init_app(app)
        cors.init_app(app)
        mail.init_app(app)

        return app
