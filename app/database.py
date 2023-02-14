from sqlalchemy import Column
from .extensions import db

Column = db.Column
relationship = db.relationship
Model = db.Model
