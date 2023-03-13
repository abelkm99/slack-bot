import datetime
from slack_bolt.adapter.flask import SlackRequestHandler
from threading import local
from flask import current_app
from slack_bolt import App
from app.Slack_APP.checkIn import register_checkIn_features
from app.Slack_APP.dailyPlan.views.add_daily_plan import get_daily_plan_view
from app.Slack_APP.dailyPlan.views.daily_plan_attachement import build_daily_plan_attachement
from app.Slack_APP.profile import register_profile_features
from app.Slack_APP.project import register_project_features
from app.Slack_APP.dailyPlan import register_daily_plan_features

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
register_checkIn_features(app=slack_app)
register_daily_plan_features(app=slack_app)



@slack_app.shortcut("check_modal")
def handle_shortcuts(ack, shortcut, body, logger, client, context):
    context['flask_app'].app_context().push()
    ack()
    logger.debug(shortcut)
    logger.debug(body)
    client.views_open(
        trigger_id=body['trigger_id'], view=get_daily_plan_view(body['user']['id']))


handler = SlackRequestHandler(app=slack_app)
