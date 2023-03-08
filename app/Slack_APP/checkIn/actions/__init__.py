import os
import time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from .checkIn import handle_checkIn
# Identifiers
# 'check-in_menu_'


def register_actions(app):
    app.view("check-in_menu_view_callback")(handle_checkIn)
    # pass
