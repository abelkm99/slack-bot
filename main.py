import os
import time
from slack_bolt import App
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)
# Sends a section block with datepicker when someone reacts with a 📅 emoji


@app.message("hi")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Please provide your heads up*"
                }
            },
            {
                "type": "input",
                "block_id": "headsup_input",
                "element": {
                    "type": "plain_text_input",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Enter your heads up here..."
                    }
                },
                "label": {
                    "type": "plain_text",
                    "text": "Heads Up"
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Submit"
                        },
                        "value": "submit",
                        "action_id": "submit_headsup"
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Cancel"
                        },
                        "value": "cancel",
                        "action_id": "cancel_headsup"
                    }
                ]
            }
        ],
        text=f"Hey there <@{message['user']}>!"
    )


@app.action("submit_headsup")
def action_submit(ack, say, context):
    # Acknowledge the action
    ack()
    say(
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*SUCCESS* \n Your heads up has been submitted"
                }
            }
        ]
    )


@app.message(":calendar:")
def show_datepicker(event, say):
    blocks = [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "Pick a date for me to remind you"},
            "accessory": {
                "type": "datepicker",
                "action_id": "datepicker_remind",
                "initial_date": "2020-05-04",
                "placeholder": {"type": "plain_text", "text": "Select a date"}
            },
        },
        {
            "type": "actions",
            "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Submit"
                        },
                        "value": "submit",
                        "action_id": "submit_headsup"
                    },
                {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Cancel"
                        },
                        "value": "cancel",
                        "action_id": "cancel_headsup"
                        }
            ]
        }
    ]
    say(
        blocks=blocks,
        text="Pick a date for me to remind you"
    )


@app.action("datepicker_remind")
def update_message(ack, body, client):
    ack()
    # ackowledge that the job has been recieved
    print(body)
    i = 0
    while(i <= 10):
        time.sleep(2)
        i += 1

    if "container" in body and "message_ts" in body["container"]:
        client.reactions_add(
            name="calendar",
            channel=body["channel"]["id"],
            timestamp=body["container"]["message_ts"],
        )

# Listen for a shortcut invocation


@app.event("message")
def handle_message_event(body):
    pass



@app.shortcut("test_id")
def open_modal(ack, body, client, say):
    ack()
    print(body)
    user = body['user']
    print("user", user)
    # client.chat_postMessage(channel=user, text="modal query triggered")
    client.views_open(
        trigger_id=body["trigger_id"],
        view={
            "title": {
                "type": "plain_text",
                "text": "Check IN",
                "emoji":True 
            },
            "type": "modal",
            "close": {
                "type": "plain_text",
                "text": "Cancel",
                "emoji": True 
            },
            "submit": {
                "type": "plain_text",
                "text": "Register",
                "emoji": True 
            },
            "blocks": [
                {
                    "type": "input",
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "plain_text_input-action",
                        "initial_value": f"{user['username']}"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Full Name",
                        "emoji": True 
                    }
                },
                {
                    "type": "input",
                    "element": {
                        "type": "static_select",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Select an item",
                            "emoji": True 
                        },
                        "options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Atrons",
                                            "emoji": True 
                                },
                                "value": "value-0"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "RateEat",
                                            "emoji": True 
                                },
                                "value": "value-1"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Lab-Connect",
                                            "emoji": True 
                                },
                                "value": "value-2"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Portal",
                                            "emoji": True 
                                },
                                "value": "value-2"
                            }
                        ],
                        "action_id": "static_select-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Curently Working On",
                        "emoji": True 
                    }
                },
                {
                    "type": "input",
                    "element": {
                        "type": "static_select",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Select an item",
                            "emoji": True 
                        },
                        "options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Full-Time",
                                    "emoji": True,
                                },
                                "value": "value-0"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Part-Time",
                                            "emoji": True
                                },
                                "value": "value-1"
                            }
                        ],
                        "action_id": "static_select-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Job Type",
                        "emoji": True
                    }
                }
            ]
        }
    )



# Initialize Flask app
from flask import Flask, request
flask_app = Flask(__name__)

# SlackRequestHandler translates WSGI requests to Bolt's interface
# and builds WSGI response from Bolt's response.
from slack_bolt.adapter.flask import SlackRequestHandler
handler = SlackRequestHandler(app)

@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)

if __name__ == "__main__":
    flask_app.run(port=3000)
    # app.start(port=int(os.environ.get("PORT", 3000)))
