import os
import time
from app.Slack_APP import handler, slack_app
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
import logging
from flask import request
from app import create_app, debug
from app.models.user import User
from config import ProdConfig, DevConfig, TestConfig
from time import sleep, time
CONFIG = DevConfig

flask_app = create_app(CONFIG)

logging.basicConfig(level=logging.DEBUG)


@flask_app.route("/")
def hello():
    # this needs some clean UP
    from app.models.project import Project
    res = Project.query.all()
    print(res)
    return "hi there\n"
# def send_dm():
#     from faker import Faker
#     from datetime import datetime
#     fake = Faker()
#     try:
#         user_id = "U04LMCX3U3G"  # replace this with your Slack user ID
#         response = slack_app.client.conversations_open(users=[user_id])
#         channel_id = response["channel"]["id"]
#         message = fake.word() + datetime.now().strftime(
#             "%Y-%m-%d %H:%M:%S")
#         slack_app.client.chat_postMessage(channel=channel_id, text=message)
#     except Exception as e:
#         print(f"Error sending message: {e}")


# send_dm()
# if not flask_app.debug or os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(func=send_dm, trigger="interval", seconds=10)
#     scheduler.start()
#     atexit.register(lambda: scheduler.shutdown())


@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)

if __name__ == "__main__":
    # slack_app.start(port=3000)
    flask_app.run(port=3000)
