# for flask api blue print
from flask import blueprints
from app.api.report import report_blueprint

api_blueprint = blueprints.Blueprint('api', __name__,url_prefix='/api/v1')

api_blueprint.register_blueprint(report_blueprint)

