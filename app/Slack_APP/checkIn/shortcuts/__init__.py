import os
import time
from slack_sdk.errors import SlackApiError
from app.Slack_APP.checkIn.views import get_checkIn_form


def handle_checkIn_shortcut(ack, body, logger, client, context):
    context['flask_app'].app_context().push()
    ack()
    logger.info(body)
    client.views_open(
        trigger_id=body['trigger_id'], view=get_checkIn_form(body))


def register_shortcuts(app):
    app.shortcut('test_id')(handle_checkIn_shortcut)
