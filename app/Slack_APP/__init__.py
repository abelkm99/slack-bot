from slack_bolt.adapter.flask import SlackRequestHandler
from threading import local
from flask import current_app
from slack_bolt import App
from app.Slack_APP.profile import register_profile_features
from app.Slack_APP.project import register_project_features
from app.Slack_APP.project.views.delete_project import delete_project_view
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


register_profile_features(app=slack_app)
register_project_features(app=slack_app)

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
    true = True
    client.views_open(trigger_id=body['trigger_id'], view = delete_project_view())
    return
    client.views_open(trigger_id=body['trigger_id'], view={
        "type": "modal",
        "title": {
                "type": "plain_text",
                "text": "My App",
                "emoji": true
        },
        "submit": {
            "type": "plain_text",
            "text": "Submit",
            "emoji": true
        },
        "close": {
            "type": "plain_text",
            "text": "Cancel",
            "emoji": true
        },
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "Delete Project",
                    "emoji": true
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*when a project is deleted it will be flaged as non and it will be archived from any future use*"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "input",
                "element": {
                    "type": "static_select",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select a project",
                        "emoji": true
                    },
                    "options": [
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "*this is plain_text text*",
                                "emoji": true
                            },
                            "value": "value-0"
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "*this is plain_text text*",
                                "emoji": true
                            },
                            "value": "value-1"
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "*this is plain_text text*",
                                "emoji": true
                            },
                            "value": "value-2"
                        }
                    ],
                    "action_id": "static_select-action"
                },
                "label": {
                    "type": "plain_text",
                            "text": "Project Name",
                    "emoji": true
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Continue",
                            "emoji": true
                        },
                        "value": "click_me_123",
                        "action_id": "actionId-0",
                        "style": "danger"
                    }
                ]
            }
        ]
    })


handler = SlackRequestHandler(app=slack_app)
