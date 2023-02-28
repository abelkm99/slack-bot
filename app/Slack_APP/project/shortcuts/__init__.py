from app.Slack_APP.project.views import *
def handle_project_shorcut(ack,body,logger, client):
    ack()
    logger.info(body)
    client.views_open(trigger_id=body['trigger_id'], view = get_project_menu())
def register_shortcuts(app):
    app.shortcut("projects")(handle_project_shorcut)