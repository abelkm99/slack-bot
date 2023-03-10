from app.database import db
from app.models.project import Project, ProjectSchema
from datetime import datetime, timedelta
from app.extensions import ma
from app.utils import *
from marshmallow import fields

from app.models.user import UserSchema


class TimeSheet(db.Model):
    __tablename__ = 'time_sheet'
    id = db.Column(db.Integer, primary_key=True)
    check_in_time = db.Column(db.DateTime, nullable=False)
    check_out_time = db.Column(db.DateTime)
    slack_id = db.Column(db.String(50), db.ForeignKey(
        'user.slack_id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey(
        'project.id'), nullable=False)
    elapsed_time = db.Column(db.Integer)

    user = db.relationship('User', backref='time_sheets')
    project = db.relationship('Project', backref='time_sheets')

    @property
    def json(self):
        return time_sheet_schema.dump(self)


class TimeSheetSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TimeSheet
    user = fields.Nested(lambda: UserSchema)
    project = fields.Nested(lambda: ProjectSchema)


time_sheet_schema = TimeSheetSchema()
time_sheets_schema = TimeSheetSchema(many=True)


def check_in(slack_id, project_name):
    # there shouldn't be any open check_in
    project = Project.query.filter_by(name=project_name).first()
    if not project:
        return {
            "success": False,
            "message": f"project with the name {project_name} doesn't exit."
        }
    # check if there exists a time_sheet row where it has been checked in but not checked out
    time_sheet = TimeSheet.query.filter_by(slack_id=slack_id).filter(
        TimeSheet.check_in_time != None, TimeSheet.check_out_time == None).first()
    if time_sheet:
        check_in_time_str = time_sheet.check_in_time.strftime(
            "%Y-%m-%d %H:%M:%S")
        return {
            "success": False,
            "message": f"user has already been checked int at {check_in_time_str}"
        }
    # else i can create a normal database string

    try:
        new_time_sheet = TimeSheet(
            check_in_time=datetime.now(), slack_id=slack_id, project_id=project.id)
        new_time_sheet.save()
    except Exception as e:
        db.session.rollback()
        return {
            "success": False,
            "message": str(e)
        }
    return {
        "success": True,
        "message": f"success fully checked in"
    }


def get_status(slack_id):
    # return the total elapsed time that is different from the current
    time_sheet = TimeSheet.query.filter_by(slack_id=slack_id).filter(
        TimeSheet.check_in_time != None, TimeSheet.check_out_time == None).first()
    return time_sheet


def check_out(slack_id):
    # check if the user has already been checked in
    time_sheet = get_status(slack_id=slack_id)
    if not time_sheet:
        return {
            "success": False,
            "message": f"user hasn't checked in yet."
        }
    check_out_time = datetime.now()
    try:
        assert (time_sheet.check_in_time < check_out_time)
        time_sheet.check_out_time = check_out_time
        time_sheet.elapsed_time = (
            time_sheet.check_out_time - time_sheet.check_in_time).total_seconds()
        time_sheet.update()
    except Exception as e:
        db.session.rollback()
        return {
            "success": False,
            "message": str(e)
        }
    return {
        "success": True,
        "message": f"success fully checked out"
    }


def get_elapsed_time(slack_id) -> str:
    # FIXME instead of slack_id take the result object from the function
    """Returns the elapsed time since the last check-in of a user.

    Args:
        slack_id (str): The Slack ID of the user.

    Returns:
        str: The elapsed time in HH:MM:SS format.
        print(convert_seconds(12319)) -> 03:25:19
    Raises:
        ValueError: If slack_id is invalid or not found.
        
    """
    result = get_status(slack_id=slack_id)
    current_time = datetime.now()
    return convert_seconds((current_time - result.check_in_time).totalseconds())


def get_state_for_date(start_date, end_date, slack_id):
    """Returns the time sheet records for a user within a date range in json format.

    Args:
        start_date (str): The start date of the range in YYYY-MM-DD format.
        end_date (str): The end date of the range in YYYY-MM-DD format.
        slack_id (str): The Slack ID of the user.

    Returns:
        list: A list of dictionaries representing the time sheet records.
        e.g 
[{'elapsed_time': 984,
  'check_in_time': '2023-03-09T17:57:26',
  'check_out_time': '2023-03-09T18:13:50',
  'id': 7,
  'project': {'name': 'Merritt, Matthews and Gonzalez',
   'id': 1,
   'archived': False}},
 {'elapsed_time': 29,
  'check_in_time': '2023-03-09T18:14:52',
  'check_out_time': '2023-03-09T18:15:21',
  'id': 8,
  'project': {'name': 'Merritt, Matthews and Gonzalez',
   'id': 1,
   'archived': False}}
]

    Raises:
        ValueError: If start_date or end_date are invalid or not found.
    """
    start_date, end_date = get_day_range(start_date, end_date)
    history = TimeSheet.query.filter_by(slack_id=slack_id)\
        .filter(TimeSheet.check_in_time >= start_date
                and TimeSheet.check_out_time <= end_date).all()
    return TimeSheetSchema(many=True, exclude=["user"]).dump(history)