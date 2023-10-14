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

    CORS_ORIGINS = "*"
    CORS_RESOURCES = r"/*"
    CORS_HEADERS = "Content-Type"
    CORS_SUPPORTS_CREDENTIALS = True
    CORS_METHODS = ["GET", "POST", "OPTIONS", "PUT", "DELETE"]
