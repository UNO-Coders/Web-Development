"""
Flask Example - Class Based Flask API using Flask-RESTful
Level - Intermediate
Author - [Raj Patra](https:github.com/raj-patra)
"""

# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask

# Flask-RESTful is an extension for Flask that adds support for quickly building REST APIs.
from flask_restful import Api, Resource
from flask_cors import CORS
from config import Config

# Flask constructor takes the name of current module (__name__) as argument.
app = Flask(__name__)

# It is always a good practice to load the app configuration from a different file.
app.config.from_object(Config())

# Enabling CORS allows our API to be used from all hosts.
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# Passing our flask app to initialize the Api class from flask_restful.
api = Api(app)


"""
General practice is to assign the index route 
to atleast one function to avoid 404 error on the
home route.

‘/’ URL is bound with hello_world() function.
"""
@app.route('/', methods=['GET'])
def index():
    return "Welcome to Demo-Flask-App", 200


# Resource classes should be inherited from the Resource class
class Greeting(Resource):
    def __init__(self):
        # Constructor not necessary for Resource classes.
        pass

    # All basic HTTP methods already exist in Resource class
    # We over-write the functions after inheriting the Resource class
    def get(self, name: str = None):
        if name:
            return f"Hello, {name}"
        else:
            return 'Please provide a name "/hello/\{name\}"'

    # Similarly other functions such as `post`, `put`, `delete`
    # can be overwritten according to the project requirements

# Every resource added into `api` becomes an endpoint for flask.
# Every resources should have a class with basic HTTP methods as its member functions.
api.add_resource(Greeting, '/hello/<name>')


if __name__ == '__main__':
    app.run(use_reloader=True)