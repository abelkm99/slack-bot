import json
import os
import time
from slack_sdk.errors import SlackApiError
from app.Slack_APP.checkIn.views import get_checkIn_form, get_checkOut_form

from app.models.time_sheet import get_status
from app.models.user import get_user_by_slack_id
from app.Slack_APP.profile.views import user_registration_form


def handle_checkIn_shortcut(ack, body, logger, client, context, shortcut):
    context['flask_app'].app_context().push()
    ack()
    slack_id = body['user']['id']
    response = client.users_info(user=slack_id)
    user = response["user"]
    if not get_user_by_slack_id(slack_id):
        client.views_open(
            trigger_id=body['trigger_id'], view=user_registration_form(body['user']['username']))
    elif get_status(slack_id):
        client.views_open(
            trigger_id=body['trigger_id'], view=get_checkOut_form(user))
    else:
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
    # app.shortcut('test')(handle_checkOut_shortcut)
