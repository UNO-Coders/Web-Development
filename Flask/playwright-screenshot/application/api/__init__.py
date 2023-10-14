"""Blueprint registration for API resources"""

from flask import Blueprint
from flask_restful import Api

snap_bp = Blueprint("api", __name__)
snap_api = Api(snap_bp)

from . import snapshot

snap_api.add_resource(snapshot.PlaywrightSnapshot, "/snapshot", endpoint="snapshot")
