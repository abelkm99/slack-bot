from slack_sdk.models.views import View
from slack_sdk.models.blocks import *
true = True

def message_hi_call_back(ack, say):
    say("I hope that this one works out")
def reaction_added(ack, say, event, client, logger, body):
    print("="*200)
    print(body)
    print("--"*200)
    print(event)
    print("--"*200)
    blocks = [{
        "type": "section",
        "text": {"type": "mrkdwn", "text": "Pick a date for me to remind you"},
        "accessory": {
              "type": "datepicker",
              "action_id": "some_action",
              "initial_date": "2020-05-04",
              "placeholder": {"type": "plain_text", "text": "Select a date"}
              }
    }]
    say(
        blocks=blocks,
        text="Pick a date for me to remind you"
    )


def app_home_opened_callback(ack, say):
    ack()
    # return say("app home opened")


def update_message(ack, say, body, respond):
    ack()

    # say("date changed")
    # Update the message to reflect the action
    user_id = body["user"]["id"]
    response_url = body["response_url"]

    # Define the message to send
    message = {
        "text": f"Thanks for clicking the button, <@{user_id}>!"
    }

    # Use the respond() function to send the message
    message = {
        "blocks": [{
            "type": "section",
            "text": {"type": "mrkdwn", "text": "Pick a date for me to remind you"},
            "accessory": {
                "type": "datepicker",
                "action_id": "some_action",
                "initial_date": "2020-05-04",
                "placeholder": {"type": "plain_text", "text": "Select a date"}
            }
        }]
    }
    respond(message)


view1 = {
    "type": "modal",
    "callback_id": "this_is_my_callback_id",
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
            "type": "section",
            "text": {
                    "type": "mrkdwn",
                    "text": "Welcome to a modal with _blocks_"
            },
            "accessory": {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "Click me!"
                },
                "action_id": "button_abc"
            }
        },
        {
            "type": "section",
            "block_id": "section678",
            "text": {
                "type": "mrkdwn",
                "text": "Pick a channel from the dropdown list"
            },
            "accessory": {
                "action_id": "text1234",
                "type": "conversations_select",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Select an item"
                }
            }
        },
        {
            "type": "section",
            "text": {
                    "type": "plain_text",
                    "text": "This is a plain text section block.",
                    "emoji": true
            }
        },
        {
            "type": "section",
            "text": {
                    "type": "mrkdwn",
                    "text": "This is a mrkdwn section block :ghost: *this is bold*, and ~this is crossed out~, and <https://google.com|this is a link>"
            }
        }
    ]
}


def home_view():
    return View(
        type="home",
        blocks=[
            SectionBlock(text="Welcome Home!"),
            SectionBlock(
                text="What would you like to do?",
                accessory=ButtonElement(
                    text="Register", action_id="register_button"
                ),
            ),
            SectionBlock(
                text="Or view your profile",
                accessory=ButtonElement(
                    text="Profile", action_id="profile_button"),
            ),
        ],
    )


def show_menu(client, body, shortcut, logger, ack):
    ack()
    logger.info(body)
    logger.info(shortcut)
    # i don't have a channel id
    # say("hello there")
    view = View(
        type="modal",
        callback_id="home_view",
        title={
            "type": "plain_text",
            "text": "Home"
        },
        blocks=[
            SectionBlock(text="Welcome Home!"),
            SectionBlock(
                text="What would you like to do?",
                accessory=ButtonElement(
                    text="Register", action_id="register_button"
                ),
            ),
            SectionBlock(
                text="Or view your profile",
                accessory=ButtonElement(
                    text="Profile", action_id="profile_button"),
            ),
        ],
    )
    client.views_open(trigger_id=body['trigger_id'], view=view1)


def handle_button(say, body, client, logger, ack):
    logger.info(body)
    ack()
    # Call views_update with the built-in client
    client.views_update(
        trigger_id=body["trigger_id"],
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
            "close": {
                "type": "plain_text",
                "text": "Back",
                "emoji": true
            },
            "submit": {
                "type": "plain_text",
                "text": "Submit",
                "emoji": true
            },
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
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Welcome to a modal with _blocks_"
                    },
                    "accessory": {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Click me!"
                        },
                        "action_id": "button_abc"
                    }
                },
            ]
        }
    )

    # say("hello mf")


def handle_text_input(ack, body, logger):
    logger.info(body)
    # Acknowledge the action request
    ack()


def handle_modal_view(say):
    view = View(
        type="modal",
        callback_id="home_view",
        title={
            "type": "plain_text",
            "text": "Home"
        },
        blocks=[
            SectionBlock(text="Welcome Home!"),
            SectionBlock(
                text="What would you like to do?",
                accessory=ButtonElement(
                    text="Register", action_id="register_button"
                ),
            ),
            SectionBlock(
                text="Or view your profile",
                accessory=ButtonElement(
                    text="Profile", action_id="profile_button"),
            ),
        ],
        # blocks=[
        #     {
        #         "type": "section",
        #         "text": {
        #             "type": "mrkdwn",
        #             "text": "What would you like to do?"
        #         }
        #     },
        #     {
        #         "type": "actions",
        #         "block_id": "register_actions",
        #         "elements": [
        #             {
        #                 "type": "button",
        #                 "text": {
        #                     "type": "plain_text",
        #                     "text": "Register"
        #                 },
        #                 "value": "register",
        #                 "action_id": "register_action"
        #             },
        #             {
        #                 "type": "button",
        #                 "text": {
        #                     "type": "plain_text",
        #                     "text": "Profile"
        #                 },
        #                 "value": "profile",
        #                 "action_id": "profile_action"
        #             }
        #         ]
        #     }
        # ]
    )
    blocks = [
        SectionBlock(
            text="This is a mrkdwn section block :ghost: *this is bold*, and ~this is crossed out~, and <https://google.com|this is a link>"),
        SectionBlock(text="Welcome Home!"),
        SectionBlock(
            text="What would you like to do?",
            accessory=ButtonElement(
                text="Register", action_id="register_button"
            ),
        ),
        SectionBlock(
            text="Or view your profile",
            accessory=ButtonElement(
                text="Profile", action_id="profile_button"),
        ),
        ActionsBlock(
            block_id="home_actions",
            elements=[
                ButtonElement(
                    text={
                        "type": "plain_text",
                        "text": "Register",
                    },
                    value="register",
                    action_id="some_action",
                ),
                ButtonElement(
                    text={
                        "type": "plain_text",
                        "text": "Profile",
                    },
                    value="profile",
                    action_id="profile_action",
                ),
            ],
        )
    ]
    say(blocks=blocks)


def register_messages(app):
    app.message("hi")(message_hi_call_back)
    app.message("modal")(handle_modal_view)
    app.event("app_home_opened")(app_home_opened_callback)
    app.event("reaction_added")(reaction_added)
    app.action("some_action")(update_message)
    app.shortcut("get_menu")(show_menu)
    app.action("button_abc")(handle_button)
    app.block_action("text1234")(handle_text_input)
