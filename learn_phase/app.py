import slack
import os
import logging
from dotenv import load_dotenv
from coin import CoinBot
from slackeventsapi import SlackEventAdapter
from flask import Flask
import json

app = Flask(__name__)

load_dotenv(dotenv_path=".env")
coin_bot = CoinBot("#general")

# msg = "Hey <!channel>, there's a new task in your queue."
slack_web_client = slack.WebClient(token=os.environ.get("TOKEN"))
slack_events_adapter = SlackEventAdapter(
    os.environ.get("EVENT"), "/slack/events", app)
BOT_ID = slack_web_client.api_call("auth.test")['user_id']

message = {}


def flip_coin(channel):
    """Craft the CoinBot, flip the coin and send the message to the channel
    """
    # Create a new CoinBot
    coin_bot = CoinBot(channel)

    # Get the onboarding message payload
    global message
    message = coin_bot.get_message_payload()

    # Post the onboarding message in Slack
    print(json.dumps(message), type(message))
    slack_web_client.chat_postMessage(
        channel=message['channel'], blocks=message['blocks'])

# When a 'message' event is detected by the events adapter, forward that payload
# to this function.


@app.route('/')
def main():

    modal = {
        "type": "modal",
        "callback_id": "gratitude-modal",
        "title": {"type": "plain_text", "text": "Gratitude Box"},
        "submit": {"type": "plain_text", "text": "Submit"},
        "close": {"type": "plain_text", "text": "Cancel"},
        "blocks": [
                {
                    "type": "input",
                    "block_id": "my_block",
                    "element": {"type": "plain_text_input", "action_id": "my_action"},
                    "label": {"type": "plain_text", "text": "Say something nice!"},
                }
        ],
    }
    json_data = {
        'channel': '@U04LMCX3U3G',
        'blocks': [
            {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn', 'text': 'Sure! Flipping a coin....\n\n'
                }
            },
            {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn', 'text': 'The result is *HEADS*',
                },
            },
            {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn',
                    'text': 'ok',
                }
            },
            {
                "type": "modal",
                "callback_id": "gratitude-modal",
                "title": {"type": "plain_text", "text": "Gratitude Box"},
                "submit": {"type": "plain_text", "text": "Submit"},
                "close": {"type": "plain_text", "text": "Cancel"},
                "blocks": [
                    {
                        "type": "input",
                        "block_id": "my_block",
                        "element": {"type": "plain_text_input", "action_id": "my_action"},
                        "label": {"type": "plain_text", "text": "Say something nice!"},
                    }
                ],
            }
        ],
    }

    slack_web_client.chat_postMessage(
        channel=json_data['channel'], blocks=json_data['blocks'])
    return "Done"


@slack_events_adapter.on("message")
def message(payload):
    """Parse the message event, and if the activation string is in the text, 
    simulate a coin flip and send the result.
    """

    # Get the event data from the payload
    event = payload.get("event", {})

    user_id = event.get("user")
    if (BOT_ID == user_id):
        return
    # Get the text from the event that came through
    text = event.get("text")

    # Check and see if the activation phrase was in the text of the message.
    # If so, execute the code to flip a coin.
    if "flip" in text.lower():
        # Since the activation phrase was met, get the channel ID that the event
        # was executed on
        channel_id = event.get("channel")

        # Execute the flip_coin function and send the results of
        # flipping a coin to the channel
        return flip_coin(f'@{user_id}')


if __name__ == "__main__":
    # Create the logging object
    # logger = logging.getLogger()

    # Set the log level to DEBUG. This will increase verbosity of logging messages
    # logger.setLevel(logging.DEBUG)

    # Add the StreamHandler as a logging handler
    # logger.addHandler(logging.StreamHandler())

    # Run our app on our externally facing IP address on port 3000 instead of
    # running it on localhost, which is traditional for development.
    app.run(host='0.0.0.0', port=3000, debug=True)
