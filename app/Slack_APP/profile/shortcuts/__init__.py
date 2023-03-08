from app.Slack_APP.profile.views import user_registered_succesfully_view, user_registration_form
from app.models.user import get_user_by_slack_id


def handle_project_shorcut(ack, shortcut, logger, client, context, body):
    ack()
    context['flask_app'].app_context().push()
    slack_id = shortcut['user']['id']
    user = get_user_by_slack_id(slack_id)
    logger.debug(user)
    if user:
        client.views_open(trigger_id=body['trigger_id'], view=user_registration_form(
            fullname=user.full_name,
            role=user.role,
            employement_status=user.employement_status,
            daily_plan_channel=user.daily_plan_channel,
            heads_up_chanel=user.headsup_channel,
            is_update=True
        ))
        return
    client.views_open(trigger_id=body['trigger_id'], view=user_registration_form(
        shortcut['user']['username']))


def register_shortcuts(app):
    app.shortcut("profile")(handle_project_shorcut)
