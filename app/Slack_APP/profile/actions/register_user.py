
from app.Slack_APP.profile.views import user_registration_form, user_registered_succesfully_view
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
        view=user_registration_form(body['user']['name'])
    )


def handel_user_registration_submission(ack, body, logger, client, context):
    context['flask_app'].app_context().push()
    # ack()
    # logger.info(body)
    view_state = body['view']['state']['values']

    try:
        response = client.users_info(user=body['user']['id'])
        profile_picture = response["user"]["profile"]["image_1024"]
        user_id = body['user']['id']
        full_name = view_state['profile_register_full_name_input_block']['profile_register_full_name_input_action']['value']
        
        role = view_state['profile_register_role_input_block']['profile_register_role_input_action']['value']
        employment_status = view_state['profile_register_selected_employement_status_block'][
            'profile_register_emoloyement_status_action']['selected_option']['text']['text']
        daily_plan_channel = view_state['profile_register_daily_plan_channel_block'][
            'profile_register_daily_plan_channel_action']['selected_conversation']
        headsup_channel = view_state['profile_register_headsup_channel_block'][
            'profile_register_headsup_channel_action']['selected_conversation']
        user = get_user_by_slack_id(user_id)
        if user:
            print("the full name is", full_name)
            user.full_name = full_name
            user.role = role
            user.employment_status = employment_status
            user.daily_plan_channel = daily_plan_channel
            user.headsup_channe = headsup_channel
            user.profile_url = profile_picture
            user.update()
            ack(response_action="update",
                view=user_registered_succesfully_view(fullname=full_name))
            return

        logger.debug([user_id, full_name, role, employment_status,
                        daily_plan_channel, headsup_channel])
        add_new_user(user_id, full_name, role, employment_status,
                        daily_plan_channel, headsup_channel, profile_picture)
        ack(response_action="update",
            view=user_registered_succesfully_view(fullname=full_name))
    except Exception as e:
        logger.error(e)
