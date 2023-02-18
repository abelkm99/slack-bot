from slack_bolt import App
from config import *
import logging

logging.basicConfig(level=logging.DEBUG)

CONFIG = DevConfig
slack_app = App(
    token=CONFIG.SLACK_BOT_TOKEN,
    signing_secret=CONFIG.SLACK_SIGNING_SECRET
)

@slack_app.middleware  # or app.use(log_request)
def log_request(logger, body, next):
    logger.debug(body)
    return next()

@slack_app.event("message")
def handle_message(say):
    say("hello mf")

from slack_bolt.adapter.flask import SlackRequestHandler
handler = SlackRequestHandler(slack_app)
