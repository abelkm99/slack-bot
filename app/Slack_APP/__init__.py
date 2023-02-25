from slack_bolt import App 
from app.Slack_APP.profile import register_profile_features
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

# register_listeners(app=slack_app)
register_profile_features(app=slack_app)


from slack_bolt.adapter.flask import SlackRequestHandler
handler = SlackRequestHandler(slack_app)