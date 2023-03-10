from app.database import db


class User(db.Model):
    __tablename__ = 'user'
    slack_id = db.Column(db.String(50), unique=True,
                         nullable=False, primary_key=True)
    full_name = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(250), nullable=False)
    employement_status = db.Column(db.String(50), nullable=False)
    daily_plan_channel = db.Column(db.String(50), nullable=False)
    headsup_channel = db.Column(db.String(50), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, slack_id, full_name, role, employement_status, daily_plan_channel, headsup_channel, is_admin=False):
        self.slack_id = slack_id
        self.full_name = full_name
        self.role = role
        self.employement_status = employement_status
        self.daily_plan_channel = daily_plan_channel
        self.headsup_channel = headsup_channel
        self.is_admin = is_admin


def add_new_user(slack_id,
                 full_name, role,
                 employement_status, daily_plan_channel, headsup_channel):
    user = User(slack_id=slack_id,
                full_name=full_name,
                role=role,
                employement_status=employement_status,
                daily_plan_channel=daily_plan_channel,
                headsup_channel=headsup_channel)
    user.save()

def get_user_by_slack_id(slack_id):
    return User.query.filter_by(slack_id = slack_id).first()