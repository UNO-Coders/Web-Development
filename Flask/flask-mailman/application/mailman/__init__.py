"""Blueprint Registration"""

from flask import Blueprint
from flask_restful import Api

from . import dispatch

mail_bp = Blueprint("util", __name__)
mail_api = Api(mail_bp)

mail_api.add_resource(dispatch.Dispatch, "/dispatch", endpoint="mailman_dispatch")
