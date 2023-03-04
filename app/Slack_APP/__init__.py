from slack_bolt.adapter.flask import SlackRequestHandler
from threading import local
from flask import current_app
from slack_bolt import App
from app.Slack_APP.profile import register_profile_features
from app.Slack_APP.project import register_project_features
from app.Slack_APP.project.views.delete_project import delete_project_confirmation_view
from config import *

import logging
logging.basicConfig(level=logging.DEBUG)

CONFIG = DevConfig

slack_app = App(
    token=CONFIG.SLACK_BOT_TOKEN,
    signing_secret=CONFIG.SLACK_SIGNING_SECRET,
)

local_storage = local()


@slack_app.middleware
def bind_flask_app(context, next):
    context['flask_app'] = current_app._get_current_object()
    next()


@slack_app.middleware  # or app.use(log_request)
def log_request(logger, body, next):
    logger.debug(body)
    return next()


register_project_features(app=slack_app)
register_profile_features(app=slack_app)

# @slack_app.action("project_add_new_project_charachter_change_action")
# def handle_some_action(ack, body, logger):
#     ack()
#     block_id = "project_add_new_project_block"
#     action_name = "project_add_new_project_charachter_change_action"
#     project_name = body['view']['state']['values'][block_id][action_name]['value']
#     logger.info(project_name)


@slack_app.shortcut("check_modal")
def handle_shortcuts(ack, body, logger, client, context):
    context['flask_app'].app_context().push()
    ack()
    logger.info(body)
    client.views_open(
        trigger_id=body['trigger_id'], view=delete_project_confirmation_view("Abel"))


@slack_app.view_closed("project_menu_view_callback")
def handle_view_closed(ack, body, logger):
    ack()
    logger.info(body)


handler = SlackRequestHandler(app=slack_app)
