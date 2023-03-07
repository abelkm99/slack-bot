import os
import time
from slack_sdk.errors import SlackApiError
from app.Slack_APP.checkIn.views import get_checkIn_menu


def handle_checkIn_shortcut(ack, body, logger, client):
    ack()
    logger.info(body)
    client.views_open(trigger_id=body['trigger_id'], view=get_checkIn_menu())


def register_shortcuts(app):
    app.shortcut('check-in')(handle_checkIn_shortcut)
