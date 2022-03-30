

from flask import Blueprint

application = Blueprint('A', __name__)  # A is python file name


@application.route('/page')
def index():
    '''
    http://0.0.0.0:5000/A/page
    '''
    return "This is function A"
