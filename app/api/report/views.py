from flask import Blueprint, jsonify
report_blueprint = Blueprint('report', __name__, url_prefix='/report/')

@report_blueprint.route('/', methods=['GET'])
def test():
    return jsonify(message = "hello")