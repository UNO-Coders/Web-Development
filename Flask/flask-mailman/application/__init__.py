"""Main Flask Application"""

from flask import Flask
from flask_cors import CORS
from flask_mailman import Mail
from flask_restful import Api

api = Api()
cors = CORS()
mail = Mail()


def init_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    with app.app_context():

        from .mailman import mail_bp

        app.register_blueprint(mail_bp, url_prefix="/mail")
        
        api.init_app(app)
        cors.init_app(app)
        mail.init_app(app)

    return app
