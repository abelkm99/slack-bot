from flask import request
from app import create_app, debug
from config import ProdConfig, DevConfig, TestConfig
from time import sleep, time
CONFIG = DevConfig

flask_app = create_app(CONFIG)

import logging
logging.basicConfig(level=logging.DEBUG)



@flask_app.route("/")
def hello():
    # this needs some clean UP
    from app.models.project import Project
    res = Project.query.all()
    print(res)
    return "hi there\n"


from app.Slack_APP import handler 
@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)

if __name__ == "__main__":
    # slack_app.start(port=3000)
    flask_app.run(port=3000)
