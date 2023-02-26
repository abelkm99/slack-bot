from slack_bolt import App 
from app.Slack_APP.profile import register_profile_features
from app.Slack_APP.project import register_project_features
from config import *

import logging
logging.basicConfig(level=logging.DEBUG)

CONFIG = DevConfig

slack_app = App(
    token=CONFIG.SLACK_BOT_TOKEN,
    signing_secret=CONFIG.SLACK_SIGNING_SECRET,
)
from flask import current_app
from threading import local

local_storage = local()

@slack_app.middleware
def bind_flask_app(context, next):
    context['flask_app'] = current_app._get_current_object()
    next()

@slack_app.middleware  # or app.use(log_request)
def log_request(logger, body, next):
    logger.debug(body)
    return next()


register_profile_features(app=slack_app)
register_project_features(app=slack_app)

# @slack_app.action("project_add_new_project_charachter_change_action")
# def handle_some_action(ack, body, logger):
#     ack()
#     block_id = "project_add_new_project_block"
#     action_name = "project_add_new_project_charachter_change_action"
#     project_name = body['view']['state']['values'][block_id][action_name]['value']
#     logger.info(project_name)


from slack_bolt.adapter.flask import SlackRequestHandler
handler = SlackRequestHandler(app=slack_app)