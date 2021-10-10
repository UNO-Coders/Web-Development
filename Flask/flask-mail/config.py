class Config(object):
    DEBUG = True
    TESTING = False
    CORS_HEADERS = 'Content-Type'

    # Credentials required to connect to the SMTP Server
    MAIL_USERNAME = "user-name"
    MAIL_PASSWORD = "password"
    MAIL_SERVER = "server"
    MAIL_SENDER = "sender"
    MAIL_PORT = 999
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    # Mail Contents
    MAIL_TITLE = "Flask-Mail Demo"
    MAIL_BODY = """
    Generic multi-line mail body.


    This is an auto generated mail.
    Please do not reply.

    Thanks.
    """