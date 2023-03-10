import json
import os
import time
from slack_sdk.errors import SlackApiError
from app.Slack_APP.checkIn.views import get_checkIn_form, get_checkOut_form

from app.models.time_sheet import TimeSheet


def handle_checkIn_shortcut(ack, body, logger, client, context):
    context['flask_app'].app_context().push()
    ack()
    # logger.info(json.dumps(body, indent=2))
    client.views_open(
        trigger_id=body['trigger_id'], view=get_checkIn_form(body))


def handle_checkOut_shortcut(ack, body, logger, client, context):
    context['flask_app'].app_context().push()
    ack()
    response = client.users_info(user=body['user']['id'])
    user = response["user"]
    client.views_open(
        trigger_id=body['trigger_id'], view=get_checkOut_form(user))


def register_shortcuts(app):
    app.shortcut('check-in')(handle_checkIn_shortcut)
    app.shortcut('test')(handle_checkOut_shortcut)
