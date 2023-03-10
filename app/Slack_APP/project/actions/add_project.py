from app.models.project import *
from app.Slack_APP.project.views import *

def handle_add_new_project_charachter_change(body, ack, logger, client, context):
    ack()
    context['flask_app'].app_context().push()
    block_id = "project_add_new_project_block"
    action_name = "project_add_new_project_charachter_change_action"
    project_name = body['view']['state']['values'][block_id][action_name]['value']
    view_id = body['view']['id']
    trigger_id = body['trigger_id']
    logger.info(project_name)
    logger.info(trigger_id)

    if get_project_by_name(name=project_name):
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
def handle_add_project_submission(ack, body, logger, context):
    context['flask_app'].app_context().push()
    block_id = "project_add_new_project_block"
    action_name = "project_add_new_project_charachter_change_action"
    project_name = body['view']['state']['values'][block_id][action_name]['value']
    project_name = project_name.strip().capitalize()
    if get_project_by_name(name=project_name):
        ack({
                "response_action": "errors",
                "errors": {
                    "project_add_new_project_block": f"The project {project_name} already exists in the database."
                }
            })
        return
    project = Project(name = project_name)
    project.save()
    logger.info(body)
    ack(response_action="update", view=project_added_succesfully_view(project_name=project_name))
