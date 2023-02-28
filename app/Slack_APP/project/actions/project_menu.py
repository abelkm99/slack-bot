from app.Slack_APP.project.views import *


def handle_open_new_project_view(ack, body, logger, client):
    ack()
    logger.info(body)
    print("right here")
    client.views_push(view_id=body["view"]["id"],
                      # String that represents view state to protect against race conditions
                      hash=body["view"]["hash"],
                      trigger_id=body["trigger_id"],
                      view=add_project_normal(project_name="project name")
                      )
