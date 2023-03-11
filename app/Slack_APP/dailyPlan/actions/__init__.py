from .add_daily_plan import handle_publish_daily_plan
def register_actions(app):
    app.action("daily_plan_ignore_action")(lambda ack: ack())
    app.view("daily_plan_view_callback")(handle_publish_daily_plan)