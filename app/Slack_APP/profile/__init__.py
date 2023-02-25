from app.Slack_APP.profile.listners.messages import register_messages
# make sure if you are using any kind of name or stuff like that
def register_profile_features(app):
    register_messages(app = app)
    # register events
    # register shortcuts
    # register slash commands
    pass