from app.models.project import *
from app.Slack_APP.project.views import *


def handle_add_new_project(body, ack, logger, client, context):
    ack()
    context['flask_app'].app_context().push()
    block_id = "project_add_new_project_block"
    action_name = "project_add_new_project_charachter_change_action"
    project_name = body['view']['state']['values'][block_id][action_name]['value']
    view_id = body['view']['id']
    trigger_id = body['trigger_id']
    logger.info(project_name)
    logger.info(trigger_id)

    if Project.query.filter_by(name=project_name).first():
        client.views_update(
            # Pass the view_id
            view_id=body["view"]["id"],
            # String that represents view state to protect against race conditions
            hash=body["view"]["hash"],
            # View payload with updated blocks
            view = add_project_error(project_name)
        )
    else:
        client.views_update(
            # Pass the view_id
            view_id=body["view"]["id"],
            # String that represents view state to protect against race conditions
            hash=body["view"]["hash"],
            # View payload with updated blocks
            view = add_project_normal(project_name)
        )
