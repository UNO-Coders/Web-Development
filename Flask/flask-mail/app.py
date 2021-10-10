"""
Flask Example - Mail Service implementation in Flask
Level - Basic
Author - [Raj Patra](https:github.com/raj-patra)
"""

# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request

from flask_mail import Mail, Message
from flask_cors import CORS
from config import Config


# Flask constructor takes the name of current module (__name__) as argument.
app = Flask(__name__)

# Initialize the flask app with the Mail constructor from the flask_mail package.
mail = Mail(app)

# It is always a good practice to load the app configuration from a different file.
app.config.from_object(Config())

# Enabling CORS allows our API to be used from all hosts.
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# Index route for the welcome message
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        return {"message": "Welcome to Demo-Flask-App"}, 200


@app.route('/sendMail', methods=["POST"])
def mail():
    # Self-explanatory
    sender = Config.MAIL_SENDER
    recipients = ["john.doe@test.com", "jane.doe@test.com"]

    title = Config.MAIL_TITLE
    body = Config.MAIL_BODY

    # Sending the mail using the current app context
    with app.app_context():
        # Starting the mail service.
        # The credentials will be fetched from flask app's config for connection.
        mail.init_app(app)
        msg = Message(subject=title, sender=sender, body=body, recipients=recipients)
        with app.open_resource("requirements.txt") as fp:
            # Demonstration of attaching a file to the mail
            msg.attach("requirements.txt", "requirements/txt", fp.read())
        mail.send(msg)

    return {"message": "E-mail Alert Sent"}, 200


