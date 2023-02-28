from app.Slack_APP.project.views import *


def handle_open_new_project_view(ack, body, logger, client):
    ack()
    logger.info(body)
    client.views_push(view_id=body["view"]["id"],
                      # String that represents view state to protect against race conditions
                      hash=body["view"]["hash"],
                      trigger_id=body["trigger_id"],
                      view=add_project_normal(project_name="project name")
                      )


def handle_open_update_project_view(ack, body, logger, client):
    ack()


def handle_open_delete_project_view(ack, body, logger, client, context):
    context['flask_app'].app_context().push()
    ack()
    logger.info(body)
    client.views_push(view_id=body["view"]["id"],
                      # String that represents view state to protect against race conditions
                      hash=body["view"]["hash"],
                      trigger_id=body["trigger_id"],
                      view=delete_project_view()
                      )
