import os
import time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from .checkIn import handle_checkIn
from .checkOut import handle_checkOut


def register_actions(app):
    app.view("check-in_menu_view_callback")(handle_checkIn)
    app.view("check-out_menu_view_callback")(handle_checkOut)
    # pass
