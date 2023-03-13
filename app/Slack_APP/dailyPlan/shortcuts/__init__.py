
from app.Slack_APP.dailyPlan.views.add_daily_plan import get_daily_plan_view
from app.models.daily_plan import get_daily_plan_for_today


def handle_daily_plan_shortcut(ack, shortcut, body, logger, client, context):
    context['flask_app'].app_context().push()
    ack()
    client.views_open(
        trigger_id=body['trigger_id'], view=get_daily_plan_view(body['user']['id']))

    return


def register_shortcts(app):
    app.shortcut("daily_plan")(handle_daily_plan_shortcut)
    pass
