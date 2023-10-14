import os

from dotenv import load_dotenv

def load_env_vars():
    """Loads environment variables from .env file."""
    load_dotenv(os.path.join(basedir, ".env"))
    return os.environ

basedir = os.path.abspath(os.path.dirname(__file__))
environment = load_env_vars()


class Config(object):
    DEBUG = False
    TESTING = False
    PROPAGATE_EXCEPTIONS = True
    SECRET_KEY = environment.get("SECRET_KEY")

    MAIL_USERNAME = environment.get("USERNAME")
    MAIL_PASSWORD = environment.get("PASSWORD")
    MAIL_SERVER = environment.get("SERVER")
    MAIL_DEFAULT_SENDER = environment.get("SENDER")
    MAIL_PORT = environment.get("PORT")
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    WTF_CSRF_ENABLED = False

    CORS_ORIGINS = "*"
    CORS_RESOURCES = r"/*"
    CORS_HEADERS = "Content-Type"
    CORS_SUPPORTS_CREDENTIALS = True
    CORS_METHODS = ["GET", "POST", "OPTIONS", "PUT", "DELETE"]
