import os
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
    print(body)
    ack()

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
                "text": "My App",
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


''' 
@app.shortcut("test_id")
def open_modal(ack, body, client):
    print("=="*1000)
    # Acknowledge the command request
    ack()
    print(body)
    # Call views_open with the built-in client
    client.views_open(
        # Pass a valid trigger_id within 3 seconds of receiving it
        trigger_id=body["trigger_id"],
        # View payload
        view={
            "type": "modal",
            # View identifier
            "callback_id": "view_1",
            "title": {"type": "plain_text", "text": "My App"},
            "submit": {"type": "plain_text", "text": "Submit"},
            "blocks": [
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": "Welcome to a modal with _blocks_"},
                    "accessory": {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "Click me!"},
                        "action_id": "button_abc"
                    }
                },
                {
                    "type": "input",
                    "block_id": "input_c",
                    "label": {"type": "plain_text", "text": "What are your hopes and dreams?"},
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "dreamy_input",
                        "multiline": True
                    }
                }
            ]
        }
    )

# Listen for a button invocation with action_id `button_abc` (assume it's inside of a modal)


@app.action("button_abc")
def update_modal(ack, body, client):
    # Acknowledge the button request
    ack()
    # Call views_update with the built-in client
    client.views_update(
        # Pass the view_id
        view_id=body["view"]["id"],
        # String that represents view state to protect against race conditions
        hash=body["view"]["hash"],
        # View payload with updated blocks
        view={
            "type": "modal",
            # View identifier
            "callback_id": "view_1",
            "title": {"type": "plain_text", "text": "Updated modal"},
            "blocks": [
                {
                    "type": "section",
                    "text": {"type": "plain_text", "text": "You updated the modal!"}
                },
                {
                    "type": "image",
                    "image_url": "https://media.giphy.com/media/SVZGEcYt7brkFUyU90/giphy.gif",
                    "alt_text": "Yay! The modal was updated"
                },
                {
                    "type": "input",
                    "block_id": "name",
                    "label": {"type": "plain_text", "text": "What are your hopes and dreams?"},
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "dreamy_input",
                        "multiline": True,
                        "value":"Abel Kidanemariam"
                    }
                }
            ]
        }
    )

# Handle a view_submission request


@app.view("view_1")
def handle_submission(ack, body, client, view, logger):
    print("-"*2000)
    print(view)
    # Assume there's an input block with `input_c` as the block_id and `dreamy_input`
    hopes_and_dreams = view["state"]["values"]["input_c"]["dreamy_input"]
    user = body["user"]["id"]
    # Validate the inputs
    errors = {}
    if hopes_and_dreams is not None and len(hopes_and_dreams) <= 5:
        errors["input_c"] = "The value must be longer than 5 characters"
    if len(errors) > 0:
        ack(response_action="errors", errors=errors)
        return
    # Acknowledge the view_submission request and close the modal
    ack()
    # Do whatever you want with the input data - here we're saving it to a DB
    # then sending the user a verification of their submission

    # Message to send user
    msg = ""
    try:
        # Save to DB
        msg = f"Your submission of {hopes_and_dreams} was successful"
    except Exception as e:
        # Handle error
        msg = "There was an error with your submission"

    # Message the user
    try:
        client.chat_postMessage(channel=user, text=msg)
    except e:
        logger.exception(f"Failed to post a message {e}")
'''
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
