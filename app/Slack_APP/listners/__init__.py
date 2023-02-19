from app.Slack_APP.listners.messages import register_messages

def register_listeners(app):
    register_messages(app)