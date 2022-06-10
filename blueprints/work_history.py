from flask import jsonify
from flask import Blueprint

# Values needed: business name, work duration, job role
# other possible values, work references, phone number

work_history_bp = Blueprint('work_history', __name__)

@work_history_bp.route('/')

def get_work_history(): 
    return 'I need to be able to give multiple values'

