import time
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

# def create_new_channel(channel_name):
#     pass
    # channel_id = None
    # for channel in app.client.conversations_list()["channels"]:
    #     if channel["name"] == channel_name:
    #         channel_id = channel["id"]
    #         break

    # # If the channel doesn't exist, create it
    # if not channel_id:
    #     response = app.client.conversations_create(name=channel_name)
    #     channel_id = response["channel"]["id"]
    #     logger.info(f"New channel created: #{channel_name}")

def handle_add_project_submission(ack, body, logger, context):
    ack()
    context['flask_app'].app_context().push()
    block_id = "project_add_new_project_block"
    action_name = "project_add_new_project_charachter_change_action"
    project_name = body['view']['state']['values'][block_id][action_name]['value']
    if get_project_by_name(name=project_name):
        ack({
                "response_action": "errors",
                "errors": {
                    "project_add_new_project_block": f"the project {project_name} already exists in the database."
                }
            })
        return
    project = Project(name = project_name)
    project.save()
    logger.info(body)

