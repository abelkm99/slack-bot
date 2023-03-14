

from app.models.time_sheet import check_out, get_elapsed_time, get_status
from app.models.project import *
from app.Slack_APP.project.views import *
from app.Slack_APP.checkIn.views import get_confirmation_dialogOUT
import json

from app.utils import convert_time_to_string


def handle_checkOut(body, ack, logger, client, context):
    context['flask_app'].app_context().push()
    # Todo: Get Rating Form Data
    slack_id = body['user']['id']
    elasped_time = get_elapsed_time(slack_id)
    check_inTime = convert_time_to_string(get_status(slack_id).check_in_time)
    response = check_out(body['user']['id'])
    if response['success'] == True:
        response = client.users_info(user=body['user']['id'])
        user = response["user"]
        ack(response_action="update",
            view=get_confirmation_dialogOUT(user, elasped_time, check_inTime))
