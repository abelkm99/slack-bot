
'''
    i want to do the following operations
    write my daily plans
        when i write my daily plans
            i want to post an atachement to the channel 
            explaining my daily plan
        I want to delete my daily plans
            is this necessary tho no
        I want to update my daily plans

    TODO
        [x] design database schema
        [x] implement the database schema
        [x] what would the flow would look like
        [x] attachment builder based on the data

    daily_plan
    daily_plan_id, user_slack_id, channel_id, datetime, message_id

    task
    daily_plan_id, task, state

    1- daily plan can have multiple tasks

    let's say for every update operation i will delete all the tasks with the daily plan ID
    and send an attachment again

    " send the attachement first "
    FLOW
        when user presses the daily plan short cut
            operations
                - check if it is an update operation or NEW
                if it is NEW
                    - fetch previous day tasks [all the tasks has state of 0]
                    - build the previous day compnent with an empty text fields for todays daily plan

                    - when user click publish
                        - first create the attachment on the channel
                        only if the attachement is created i will create the database and commit
                if it is not NEW
                    build the components but this time it has to be populated
                    SO I will have this database where i would post the result
'''
from typing import List, Optional

from sqlalchemy import func
from app.database import db
from app.models.project import Project, ProjectSchema
from app.models.user import User, UserSchema

from datetime import datetime, timedelta
from app.extensions import ma
from app.utils import *
from marshmallow import fields

task_types = ["DEVELOPMENT", "PROBLEM_SOLVING"]

class DailyPlan(db.Model):
    __tablename__ = "daily_plan"
    id = db.Column(db.Integer, primary_key=True)
    slack_id = db.Column(db.String(50), db.ForeignKey(
        'user.slack_id'), nullable=False)
    channel_id = db.Column(db.String(50), nullable=False)
    time_published = db.Column(db.DateTime, nullable=False)
    message_id = db.Column(db.String(50), nullable=False)

    tasks = db.relationship('Task', backref='daily_plan')


class Task(db.Model):
    __tablename__ = "task"
    id = db.Column(db.Integer, primary_key=True)
    daily_plan_id = db.Column(db.Integer, db.ForeignKey(
        'daily_plan.id'
    ), nullable=False)
    task = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    state = db.Column(db.Integer, nullable=False, default=0)


def get_previous_plan(slack_id) -> DailyPlan:
    current_dt = datetime.combine(datetime.now(), time.min)
    daily_plan = DailyPlan.query.filter_by(slack_id=slack_id)\
        .filter(DailyPlan.time_published < current_dt)\
        .order_by(DailyPlan.time_published.desc())\
        .first()
    return daily_plan


def create_daily_plan(user: User,
                      message_id: str,
                      developments: List[str],
                      problem_solvings: List[str]
                      ) -> DailyPlan:
    # check if is the first one
    # else delete all the previous one
    dp = DailyPlan(
        slack_id=user.slack_id,
        channel_id=user.daily_plan_channel,
        time_published=datetime.now(),
        message_id=message_id
    )
    for task in developments:
        dp.tasks.append(Task(task=task, type=task_types[0]))
    for task in problem_solvings:
        dp.tasks.append(Task(task=task, type=task_types[1]))
    return dp


def update_daily_plan_tasks(
    current_daily_plan: DailyPlan, developments: List[str],
    problem_solvings: List[str]
):
    Task.query.filter_by(daily_plan_id=current_daily_plan.id).delete()
    for task in developments:
        current_daily_plan.tasks.append(Task(task=task, type=task_types[0]))
    for task in problem_solvings:
        current_daily_plan.tasks.append(Task(task=task, type=task_types[1]))
    return current_daily_plan 


def update_prev_date_state(prev_plan: DailyPlan, completed_task_ids: set) -> DailyPlan:
    for task in prev_plan.tasks:
        task.state = 1
        if task.id in completed_task_ids:
            task.state = 1
        else:
            task.state = 0
    return prev_plan


def get_daily_plan_for_today(slack_id: str) -> Optional[DailyPlan]:
    today = date.today()
    return DailyPlan.query.filter_by(slack_id=slack_id).filter(func.date(DailyPlan.time_published) == today).first()
