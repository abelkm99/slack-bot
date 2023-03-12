

from app.models.time_sheet import check_out
from app.models.project import *
from app.Slack_APP.project.views import *
from app.Slack_APP.checkIn.views import get_confirmation_dialog
import json

def handle_checkOut(body,ack, logger,client,context):
    context['flask_app'].app_context().push()
    # Todo: Get Rating Form Data
    response = check_out(body['user']['id'])
    if response['success'] == True:
        response = client.users_info(user=body['user']['id'])
        user = response["user"]
        ack(response_action="update",
            view=get_confirmation_dialog(user))