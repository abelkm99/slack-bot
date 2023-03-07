
from app.Slack_APP.profile.views import get_register_form, user_registered_succesfully_view
from app.models.user import add_new_user, get_user_by_slack_id


def handel_user_registration(ack, body, logger, client, context):
    ack()
    context['flask_app'].app_context().push()
    # if the user is registered
    logger.debug(body)
    client.views_push(
        # Pass the view_id
        view_id=body["view"]["id"],
        # Pass the trigger id
        trigger_id=body["trigger_id"],
        # String that represents view state to protect against race conditions
        hash=body["view"]["hash"],
        # View payload with updated blocks
        view=get_register_form(body['user']['name'])
    )


def handel_user_registration_submission(ack, body, logger, client, context):
    context['flask_app'].app_context().push()
    # ack()
    # logger.info(body)
    view_state = body['view']['state']['values']

    user_id = body['user']['id']
    if get_user_by_slack_id(user_id):
        ack({
            "response_action": "errors",
            "errors": {
                "profile_register_full_name_input_block": f"User already exists in the database."
            }
        })
        return
        ack(response_action="push",
            view=user_registered_succesfully_view(fullname="yabkalu"))
        return

    full_name = view_state['profile_register_full_name_input_block']['profile_register_full_name_input_action']['value']
    role = view_state['profile_register_role_input_block']['profile_register_role_input_action']['value']
    employment_status = view_state['profile_register_selected_employement_status_block'][
        'profile_register_emoloyement_status_action']['selected_option']['text']['text']
    daily_plan_channel = view_state['profile_register_daily_plan_channel_block'][
        'profile_register_daily_plan_channel_action']['selected_conversation']
    heads_up_channel = view_state['profile_register_heads_up_channel_block'][
        'profile_register_heads_up_channel_action']['selected_conversation']
    logger.info([user_id, full_name, role, employment_status,
                daily_plan_channel, heads_up_channel])

    add_new_user(user_id, full_name, role, employment_status,
                 daily_plan_channel, heads_up_channel)
    ack(response_action="update",
        view=user_registered_succesfully_view(fullname=full_name))
