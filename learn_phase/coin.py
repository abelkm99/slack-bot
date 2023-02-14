import random


class CoinBot:
    # Create a constant that contains the default text for the message
    BUTTON = {
        "type": "section",
        "text": {
            "type": "plain_text",
            "text": "Click Me"
        },
        "value": "click_me_123",
        "action_id": "button"
    }


    btn_2 = {
        "text": "Would you like to play a game?",
        "attachments": [
            {
                "text": "Choose a game to play",
                "fallback": "You are unable to choose a game",
                "callback_id": "wopr_game",
                "color": "#3AA3E3",
                "attachment_type": "default",
                "actions": [
                    {
                        "name": "game",
                        "text": "Chess",
                        "type": "button",
                        "value": "chess"
                    },
                    {
                        "name": "game",
                        "text": "Falken's Maze",
                        "type": "button",
                        "value": "maze"
                    },
                    {
                        "name": "game",
                        "text": "Thermonuclear War",
                        "style": "danger",
                        "type": "button",
                        "value": "war",
                        "confirm": {
                            "title": "Are you sure?",
                            "text": "Wouldn't you prefer a good game of chess?",
                            "ok_text": "Yes",
                            "dismiss_text": "No"
                        }
                    }
                ]
            }
        ]
    }
    COIN_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Sure! Flipping a coin....\n\n"
            ),
        },
    }
    def __init__(self, channel) -> None:
        self.channel = channel

    def _flip_coin(self):
        rand_int = random.randint(0, 1)
        if rand_int == 0:
            results = "Heads"
        else:
            results = "Tails"
        text = f"The result is *{results}*"
        return {"type": "section", "text": {"type": "mrkdwn", "text": text}},
    # Craft and return the entire message payload as a dictionary.
    def get_message_payload(self):
        return {
            "channel": self.channel,
            "blocks": [
                self.COIN_BLOCK,
                *self._flip_coin(),
            ],
        }
