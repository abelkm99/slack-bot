from app.database import db

class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    archived = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self) -> str:
        return f"<Project {self.name}>"
    
def add_project(name):
    if not get_project_by_name(name=name):
        project = Project(name = name) 
        db.session.add(project)
        db.session.commit()
        return project
    return None

def get_project_by_name(name):
    return Project.query.filter_by(name=name).first()

def get_active_projects():
    return Project.query.filter_by(archived=0).all()
def get_archived_projects():
    return Project.query.filter_by(archived=1).all()
def get_all_projects():
    return Project.query.all()