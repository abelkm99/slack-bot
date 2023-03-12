from app.models.project import *
from app.Slack_APP.project.views import *
from app.Slack_APP.checkIn.views import get_confirmation_dialog
from app.models.time_sheet import check_in, get_status
import json


def handle_checkIn(body, ack, logger, client, context):
    # ack()
    context['flask_app'].app_context().push()
    project = body['view']['state']['values']['check-in_menu_select_project']['static_select-action']['selected_option']['value']
    response = check_in(body['user']['id'], project)

    if response['success'] == True:
        response = client.users_info(user=body['user']['id'])
        user = response["user"]
        ack(response_action="update",
            view=get_confirmation_dialog(user))
    # Todo : Response werror
    # client.views_update(
    #     # Pass the view_id
    #     view_id=body["view"]["id"],
    #     # String that represents view state to protect against race conditions
    #     hash=body["view"]["hash"],
    #     # View payload with updated blocks
    #     view=get_confirmation_dialog())
