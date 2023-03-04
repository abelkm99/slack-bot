from app.Slack_APP.profile.views import get_profile_menu


def handle_project_shorcut(ack, body, logger, client):
    ack()
    logger.info(body)
    client.views_open(trigger_id=body['trigger_id'], view=get_profile_menu())


def profile_shortcuts(app):
    app.shortcut("profile")(handle_project_shorcut)
