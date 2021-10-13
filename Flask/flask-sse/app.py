"""
Flask Example - Server side events in Flask
Level - Intermediate
Author - [Raj Patra](https:github.com/raj-patra)
"""

# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask,jsonify
from flask_sse import sse
import logging
from apscheduler.schedulers.background import BackgroundScheduler
from flask_cors import CORS
import datetime
from helper import get_data,get_schd_time

# Flask constructor takes the name of current module (__name__) as argument.
app = Flask(__name__)

# Enabling CORS allows our API to be used from all hosts.
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# Keeping the redis url in flask app config
# flask-sse uses redis to store and send data during events
app.config["REDIS_URL"] = "redis://redis"

# sse becomes a blueprint for our flask application and bound to a specific route
app.register_blueprint(sse, url_prefix='/stream')

# Used for logging server side events, among others
log = logging.getLogger('apscheduler.executors.default')
log.setLevel(logging.INFO)
fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
h = logging.StreamHandler()
h.setFormatter(fmt)
log.addHandler(h)

def server_side_event():
    """ Function to publish server side event """
    with app.app_context():
        sse.publish(get_data(), type='event')
        print("Event Scheduled at ",datetime.datetime.now())

# The Background scheduler will send mock data through the stream in intervals
# The client can keep listening on this route for events
sched = BackgroundScheduler(daemon=True)
sched.add_job(server_side_event,'interval',seconds=get_schd_time())
sched.start()

# Index route
@app.route('/')
def index():
    # get_data uses Faker to generate fake data
    return jsonify(get_data())


if __name__ == '__main__':
   app.run(debug=True,host='0.0.0.0',port=5000)