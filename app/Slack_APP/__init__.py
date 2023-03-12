from slack_bolt.adapter.flask import SlackRequestHandler
from threading import local
from flask import current_app
from slack_bolt import App
from app.Slack_APP.checkIn import register_checkIn_features
from app.Slack_APP.dailyPlan.views.add_daily_plan import get_daily_plan_view
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

# @slack_app.action("project_add_new_project_charachter_change_action")
# def handle_some_action(ack, body, logger):
#     ack()
#     block_id = "project_add_new_project_block"
#     action_name = "project_add_new_project_charachter_change_action"
#     project_name = body['view']['state']['values'][block_id][action_name]['value']
#     logger.info(project_name)


@slack_app.shortcut("check_modal")
def handle_shortcuts(ack, shortcut, body, logger, client, context):
    context['flask_app'].app_context().push()
    ack()
    logger.debug(shortcut)
    logger.debug(body)
    client.views_open(
        trigger_id=body['trigger_id'], view=get_daily_plan_view(body['user']['id']))


@slack_app.message("HOW")
def handle_message(event, say, logger, client):
    logger.debug(event)
    text = event["text"]
    user = event["user"]
    channel = event["channel"]

    # # Reply to the user with "Hi"
    import time

    user_id = "U04LMCX3U3G"  # replace this with your Slack user ID
    response = slack_app.client.conversations_open(users=[user_id])
    channel_id = response["channel"]["id"]

    attachment = {
        "fallback": "How is your day going so far?",
        "title": "How is your day going so far?",
        "color": "#3AA3E3",
        "footer": "My Bot",
        "ts": int(time.time())
    }

    updated_attachment = {
        "fallback": "Saturday's Report / Mar 4",
        "title": "Saturday's Report / Mar 4",
        "fields": [
            {
                "title": "A2SV Development",
                "value": "Sync with product team\nWork on user flows related to uploading materials\nSync with Selman",
                "short": False
            },
            {
                "title": "A2SV Problem Solving",
                "value": "Solve leetcode daily question",
                "short": False
            }
        ],
        "color": "#36a64f",
        "footer": "My Bot",
        "ts": int(time.time())
    }
    updated_attachment = {
        "color": "#36a64f",
        "blocks": [
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": "                                 *-            ABEL             -* \n Here's :"
                    },
                    {
                        "type": "mrkdwn",
                        "text": "                                 *-            ABEL             -* \n Here's your updated attachment:"
                    },
                    {
                        "type": "mrkdwn",
                        "text": "                                 *-            ABEL             -* \n Here's :"
                    },
                    {
                        "type": "mrkdwn",
                        "text": "                                 *-            ABEL             -* \n Here's your updated attachment:"
                    }
                ]
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": "*Saturday's Report / Mar 4*\n• A2SV Development\nSync with product team\nWork on user flows related to uploading materials\nSync with Selman\n• A2SV Problem Solving\nSolve leetcode daily question"
                    }
                ]
            }
        ]
    }
    response = client.chat_postMessage(
        channel="#general",
        text="Daily Tasks Report",
        attachments=[attachment, updated_attachment, attachment, updated_attachment]
    )
#     ts = message["ts"]

#     # Wait for 20 seconds
#     ## should i use should i use
#     time.sleep(5)


#     # Update the message with an attachment
#     attachment = {
#         "fallback": "How is your day going so far?",
#         "title": "How is your day going so far?",
#         "text": f"Hi <@{user}>, how's it going?",
#         "color": "#3AA3E3",
#         "footer": "My Bot",
#         "ts": int(time.time())
#     }
#     slack_app.client.chat_update(
#         channel=channel,
#         ts=ts,
#         attachments=[attachment, updated_attachment]
#     )
handler = SlackRequestHandler(app=slack_app)
