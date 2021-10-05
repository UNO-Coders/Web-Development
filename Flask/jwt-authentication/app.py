"""
Flask Example - JWT Autentication in Flask
Level - Intermediate
Author - [Raj Patra](https:github.com/raj-patra)
"""

# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request

# Flask-RESTful is an extension for Flask that adds support for quickly building REST APIs.
from flask_cors import CORS
from config import Config

"""JSON Web Token is a proposed Internet standard for creating data with optional 
signature and/or optional encryption whose payload holds JSON.
 
The tokens are signed either using a private secret or a public/private key."""
import jwt

# Flask constructor takes the name of current module (__name__) as argument.
app = Flask(__name__)

# It is always a good practice to load the app configuration from a different file.
app.config.from_object(Config())

# Enabling CORS allows our API to be used from all hosts.
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# This function whitelists certain functions from auth checking process.
# It assigns an attribute `_no_auth` which will be checked prior to auth validation.
def exclude_from_auth(func):
    func._no_auth = True
    return func

# The before_request decorator makes sure the encolsed function
# is called before every request. Pretty handy to check for authentication.
@app.before_request
def check_auth():
    # Try-Catch can be used to trigger an exception incase
    # the request signature fails to validate (Unauthorizer)
    try:
        # If a valid endpoint is requested
        if request.endpoint in app.view_functions:
            # If `_no_auth` attribute does not exist
            if not hasattr(app.view_functions[request.endpoint], '_no_auth'):
                token = request.headers.get('Authorization').split(" ")[1]
                """
                Common Practice of Sending JWT Token in a request
                
                Headers:
                    Authorization: Bearer <token>
                    
                """
                jwt.decode(token, key=app.config["SECRET_KEY"], algorithms=["HS256"])
                # If decoding completes with no error we can proceed to
                # provide access to the resource
        else:
            return {"message": "Requested enpoint does not exist"}, 404
    except Exception as e:
        # If exception occurs it would be if the signature decode fails
        print(str(e))
        return {"message": "Unauthorized Request"}, 401


# Since index routes is generally not a protected route
# we can add exclude_from_auth decorater
@app.route('/', methods=["GET", "POST"])
@exclude_from_auth
def index():
    if request.method == 'GET':
        return {"message": "Welcome to Demo-Flask-App"}, 200


# This route would take JWT as Authorization Header to work
@app.route("/hello/<user_name>")
def say_hello(user_name: str = None):
    if user_name:
        return f"Hello, {user_name}"
    else:
        return 'Please provide a name "/hello/\{user_name\}"'


# Example: How to send JWT token to Client which can be used by client to request other resources
# This route can be used to create JWT tokens for a user in session
@app.route("/signup", methods=["POST"])
def signup():
    body = request.json
    body["token"] = jwt.encode(body, key=app.config["SECRET_KEY"], algorithm="HS256")
    return body


if __name__ == '__main__':
    app.run(use_reloader=True)