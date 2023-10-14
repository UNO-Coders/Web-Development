"""Module to handle /api/snapshot endpoint"""

import base64
from io import BytesIO

from flask import current_app as app
from flask import request, send_file
from flask_restful import Resource

from application._helpers import schemas
from application.snapper import PlaywrightSnapper


class PlaywrightSnapshot(Resource):
    """Generic Snapshot Resource"""

    def __init__(self) -> None:
        pass # Constructor not needed for this resource

    def get(self):
        """GET /api/snapshot - For single page
        
        Returns: Downloads Base64 encoded image as a file
        """

        try:
            self.snapper = PlaywrightSnapper(render_html=False)

            schema = schemas.SnapshotURLSchema(unknown="include")
            validated_args = schema.load(request.args)

            download_name = "Untitled.png"

            response = self.snapper.process_snapshot(pages=[validated_args])
            image_data = BytesIO(base64.b64decode(response[0]["base64_content"]))

            return send_file(
                image_data, mimetype="image/png",
                download_name=download_name, as_attachment=validated_args.get("attachment", False)
            )
        except Exception as error:
            return {
                "error": str(error),
                "error_code": error.__traceback__.tb_lineno
            }, 500

    def post(self):
        """POST /api/snapshot - For multiple pages
        
        Returns: List of Base64 encoded images as a JSON response.
        """

        try:
            self.snapper = PlaywrightSnapper(render_html=True)

            schema = schemas.SnapshotMultipleSchema(unknown="include")
            validated_payload = schema.load(request.json)

            response = self.snapper.process_snapshot(pages=validated_payload.get("pages"))

            return {
                "pages": response,
            }, 200

        except Exception as error:
            return {
                "error": str(error),
                "error_code": error.__traceback__.tb_lineno
            }, 500