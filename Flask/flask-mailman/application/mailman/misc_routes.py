"""Miscellaneous Routes for the client side"""

from flask import current_app as app
from flask import request

@app.route("/")
def index():
    """Returns the index page"""

    return {
        "about": "Flask Mailman",
        "details": "Middleware service used to send emails",
        "version": "1.0.0"
    }, 200

@app.before_request
def check_endpoint():
    """Checks if the endpoint exists"""

    if request.endpoint not in app.view_functions:
        return {"message": "Requested endpoint does not exist"}, 404
