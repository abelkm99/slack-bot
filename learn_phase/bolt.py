# import os
# from slack_bolt import App
# from dotenv import load_dotenv
# import os
# from slack_bolt import App

# load_dotenv(dotenv_path=".env")

# # Initializes your app with your bot token and signing secret
# app = App(
#     token=os.environ.get("SLACK_BOT_TOKEN"),
#     signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
# )


# @app.event("app_home_opened")
# def say_hello(say,event):
#     if event['tab'] == "home":
#         say("hi")


# @app.message("hello")
# def message_hello(message, say):
#     # say() sends a message to the channel where the event was triggered
#     say(
#         blocks = [
#             {
#                 "type": "section",
#                 "text": {
#                     "type": "mrkdwn",
#                     "text": "*Please provide your heads up*"
#                 }
#             },
#             {
#                 "type": "input",
#                 "block_id": "headsup_input",
#                 "element": {
#                     "type": "plain_text_input",
#                     "placeholder": {
#                         "type": "plain_text",
#                         "text": "Enter your heads up here..."
#                     }
#                 },
#                 "label": {
#                     "type": "plain_text",
#                     "text": "Heads Up"
#                 }
#             },
#             {
#                 "type": "actions",
#                 "elements": [
#                     {
#                         "type": "button",
#                         "text": {
#                             "type": "plain_text",
#                             "text": "Submit"
#                         },
#                         "value": "submit",
#                         "action_id": "submit_headsup"
#                     },
#                     {
#                         "type": "button",
#                         "text": {
#                             "type": "plain_text",
#                             "text": "Cancel"
#                         },
#                         "value": "cancel",
#                         "action_id": "cancel_headsup"
#                     }
#                 ]
#             }
#         ],
#         text=f"Hey there <@{message['user']}>!"
#     )


# @app.action("button_click")
# def action_button_click(body, ack, say):
#     # Acknowledge the action
#     ack()
#     say(f"<@{body['user']['id']}> clicked the button")

# @app.action("my_action")
# def get_the_time(body,ack,say):
#     ack()
#     print(body)
#     say("FARM CLICKED")

# # Start your app
# if __name__ == "__main__":
#     app.start(port=int(os.environ.get("PORT", 3000)))
import os
from slack_bolt import App 
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)


@app.event("app_home_opened")
def say_hello(say,event):
    if event['tab'] == "home":
        say("hi")


@app.message("hello")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(
        blocks = [
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

@app.action("cancel_headsup")
def cancel_headsup(ack, say, action):
    ack()
    # Delete the original message
    say("Heads up cancelled.", delete_original=True)

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
