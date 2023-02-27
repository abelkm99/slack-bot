from app.Slack_APP.project.actions import register_actions
from app.Slack_APP.project.shortcuts import register_shortcuts
def register_project_features(app):
    register_actions(app=app)
    register_shortcuts(app=app)