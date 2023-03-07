from app.Slack_APP.profile.shortcuts import register_shortcuts
from app.Slack_APP.profile.actions import register_actions

def register_profile_features(app):
    register_shortcuts(app=app)
    register_actions(app=app)