from flask import Blueprint, jsonify
from app.models.user import User
report_blueprint = Blueprint('report', __name__, url_prefix='/report/')

@report_blueprint.route('/', methods=['GET'])
def test():
    users = User.query.all()
    return jsonify(message = "hello")