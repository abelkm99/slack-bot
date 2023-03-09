from app.database import db
from app.models.project import Project
from datetime import datetime, timedelta
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

def check_in(slack_id, project_name):
    # there shouldn't be any open check_in
    project = Project.query.filter_by(name = project_name).first()
    if not project:
        return {
            "success":False,
            "message":f"project with the name {project_name} doesn't exit."    
        }
    # check if there exists a time_sheet row where it has been checked in but not checked out
    time_sheet = TimeSheet.query.filter_by(slack_id=id).filter(TimeSheet.check_in_time != None, TimeSheet.check_out_time == None).all()
    if time_sheet:
        check_in_time_str = time_sheet.check_in_time.strftime("%Y-%m-%d %H:%M:%S")
        return {
            "success":False,
            "message":f"user has already been checked int at {check_in_time_str}"
        }
    # else i can create a normal database string

    new_time_sheet = TimeSheet(check_in_time = datetime.now(), slack_id = slack_id, project_id = project.id)
    new_time_sheet.save()
    return {
        "success":True,
        "message":f"success fully checked in"
    }
def get_status(slack_id):
    # return the total elapsed time that is different from the current
    pass
def check_out(slack_id):
    # check if the user has already been checked in
    pass