from app.models.user import get_user_by_slack_id


def handle_profile_change(body, logger, context):
    context['flask_app'].app_context().push()
    logger.debug(body)
    user = get_user_by_slack_id(body['event']['user']['id'])
    new_image_url = body['event']['user']['profile']['image_1024']
    user.profile_url = new_image_url
    user.save()
    

def register_events(app):
    app.event("user_change")(handle_profile_change)
