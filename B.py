from flask import Blueprint

application = Blueprint('B', __name__)


@application.route('/page')
def index():
    return "This is function B"
