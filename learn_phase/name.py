import os
from slack_bolt import App
from dotenv import load_dotenv
import requests

load_dotenv(dotenv_path=".env")

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

@app.message("start")
def open_modal(ack, message):
    response = requests.post(
        "https://slack.com/api/views.open",
        json={
            "trigger_id": message["trigger_id"],
            "view": {
                "type": "modal",
                "title": {
                    "type": "plain_text",
                    "text": "My Modal"
                },
                "blocks": [
                    {
                        "type": "input",
                        "block_id": "name_input",
                        "label": {
                            "type": "plain_text",
                            "text": "Enter your name"
                        },
                        "element": {
                            "type": "plain_text_input",
                        }
                    },
                    {
                        "type": "actions",
                        "block_id": "submit_action",
                        "elements": [
                            {
                                "type": "button",
                                "text": {
                                    "type": "plain_text",
                                    "text": "Submit"
                                },
                                "value": "submit"
                            }
                        ]
                    }
                ],
                "submit": {
                    "type": "plain_text",
                    "text": "Submit"
                }
            }
        },
        headers={
            "Content-type": "application/json; charset=utf-8",
            "Authorization": f"Bearer {app.bot_token}"
        }
    )
    ack(response=response)

@app.view("collect_info_form")
def collect_info_form_submit(ack, view, payload):
    ack()
    name = view["state"]["values"]["name_input"]["name_input"]["value"]
    app.client.chat_postMessage(channel=payload["user"]["id"],text=f"Your name is {name}")
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))