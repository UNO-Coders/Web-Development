"""Request schemas for Utility based functions"""

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileSize
from wtforms import EmailField, FieldList, StringField, TextAreaField
from wtforms.validators import InputRequired

MAIL_ALLOWED_FILE_TYPES = [
    "jpg", "png", "gif", "bmp", "tif",
    "doc", "docx", "ppt", "pptx", "xls", "xlsx", "pdf",
    "txt", "rtf", "json", "html",
    "zip",
]


class EmailForm(FlaskForm):
    """Form Schema for Email Alert"""

    recipients = FieldList(
        EmailField(
            label="Mail Recipient",
            validators=[InputRequired()]
        ),
        min_entries=1,
        separator="_"
    )
    cc = FieldList(
        EmailField(label="Mail Recipient - CC"),
        min_entries=0,
        separator="_"
    )
    bcc = FieldList(
        EmailField(label="Mail Recipient - BCC"),
        min_entries=0,
        separator="_"
    )
    reply_to = FieldList(
        EmailField(label="Mail Reply To"),
        min_entries=0,
        separator="_"
    )
    subject = StringField(
        label="Mail Subject",
        validators=[InputRequired()]
    )
    body = TextAreaField(
        label="Mail Body - text/plain",
        validators=[InputRequired()]
    )
    html = TextAreaField(
        label="Mail Body - text/html",
    )
    attachments = FieldList(
        FileField(
            validators=[
                FileAllowed(MAIL_ALLOWED_FILE_TYPES, "Invalid Filetype detected."),
                FileSize(max_size=2.5e7)
            ]
        ),
        min_entries=0,
        separator="_"
    )
