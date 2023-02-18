from slack_bolt import App
from app import create_app, debug
from flask import request
from config import ProdConfig, DevConfig, TestConfig
from time import sleep, time

import logging
logging.basicConfig(level=logging.DEBUG)

CONFIG = DevConfig
flask_app = create_app(CONFIG)


@flask_app.route("/")
def hello(): return "hi there\n"

from app.Slack_APP import handler 
@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)

if __name__ == "__main__":
    # slack_app.start(port=3000)
    flask_app.run(port=3000)
