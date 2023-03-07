from app.Slack_APP.checkIn.actions import register_actions
from app.Slack_APP.checkIn.shortcuts import register_shortcuts


def register_checkIn_features(app):
    register_actions(app=app)
    register_shortcuts(app=app)
