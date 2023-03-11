from app.Slack_APP.dailyPlan.actions import register_actions
from app.Slack_APP.dailyPlan.shortcuts import register_shortcts
def register_daily_plan_features(app):
    register_actions(app=app)
    register_shortcts(app=app)