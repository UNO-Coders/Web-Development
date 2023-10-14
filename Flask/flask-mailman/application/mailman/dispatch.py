"""Module to handle the email alert"""

from flask import current_app as app
from flask_mailman import EmailMessage
from flask_restful import Resource

from application._helpers import schema


class Dispatch(Resource):
    """Sends request based email through auto notification"""

    def __init__(self) -> None:
        self.form = schema.EmailForm()
    
    def post(self) -> tuple:
        if self.form.validate():
            attachments = []
            for attachment in self.form.attachments.data:
                attachments.append(
                    (attachment.filename, attachment.stream.read(), attachment.content_type)
                )

            message = EmailMessage(
                subject=self.form.subject.data,
                body=self.form.html.data if self.form.html.data else self.form.body.data,
                to=self.form.recipients.data,
                cc=self.form.cc.data,
                bcc=self.form.bcc.data,
                reply_to=self.form.reply_to.data,
                attachments=attachments
            )
            message.content_subtype = "html" if self.form.html.data else "plain"

            if not app.config["TESTING"]:
                with app.app_context():
                    message.send()

            return {
                "message": "Email Alert Status: Success",
            }, 200

        else:
            return {
                "message": "Email Alert Status: Failure",
                "error": "Invalid/Missing form data detected."
            }, 400
