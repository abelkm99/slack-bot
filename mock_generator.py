from faker import Faker
from app.models import *
from app import create_app
from config import *
import random

app = create_app(DevConfig)
app.app_context().push()

fake = Faker()


def clear_database():
    try:
        db.drop_all()
        db.create_all()
    except:
        db.session.rollback()

def create_projects(count=5):
    # Generate mock projects
    projects = []
    for i in range(count):
        name = fake.company()
        project = Project(name=name)
        projects.append(project)

    try:
        db.session.add_all(projects)
        db.session.commit()
    except:
        db.session.rollback()


# Generate mock users


def create_users(count=2):

    users = []
    for i in range(count):
        slack_id = fake.user_name()
        full_name = fake.name()
        role = fake.job()
        employement_status = fake.word(
            ext_word_list=['Full-Time', 'Part-Time', 'Intern'])
        daily_plan_channel = fake.word()
        headsup_channel = fake.word()
        user = User(slack_id=slack_id, full_name=full_name, role=role,
                    employement_status=employement_status, daily_plan_channel=daily_plan_channel,
                    headsup_channel=headsup_channel)
        users.append(user)

    try:
        db.session.add_all(users)
        db.session.commit()
    except:
        db.session.rollback()

def create_time_sheet(count=100):
    projects = Project.query.all()
    users = User.query.all()

    time_sheets = []
    for i in range(count):
        check_in_time = fake.date_time_this_month(
            before_now=True, after_now=False, tzinfo=None)
        check_out_time = fake.date_time_between(
            start_date=check_in_time, end_date=f"+{random.randint(1,8)}h", tzinfo=None)
        slack_id = fake.random_element(users).slack_id
        project_id = fake.random_element(projects).id
        elapsed_time = (check_out_time - check_in_time).seconds
        time_sheet = TimeSheet(check_in_time=check_in_time, check_out_time=check_out_time,
                               slack_id=slack_id, project_id=project_id, elapsed_time=elapsed_time)
        time_sheets.append(time_sheet)

    try:
        db.session.add_all(time_sheets)
        db.session.commit()
    except:
        db.session.rollback()
