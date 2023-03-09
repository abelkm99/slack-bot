from app.database import db

class TimeSheet(db.Model):
    __tablename__ = 'time_sheet'
    id = db.Column(db.Integer, primary_key=True)
    check_in_time = db.Column(db.DateTime, nullable=False)
    check_out_time = db.Column(db.DateTime, nullable=False)
    slack_id = db.Column(db.String(50), db.ForeignKey(
        'user.slack_id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey(
        'project.id'), nullable=False)
    elapsed_time = db.Column(db.Integer)

    user = db.relationship('User', backref='time_sheets')
    project = db.relationship('Project', backref='time_sheets')
