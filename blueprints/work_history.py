from flask import jsonify
from flask import Blueprint

# Values needed: business name, work duration, job role
# other possible values, work references, phone number

work_history_bp = Blueprint('work_history', __name__)

@work_history_bp.route('/')

def get_work_history():
    return 'This will get the work history data'

# So how I went about this was completely wrong
# make data base first, pass down data from database 
# jsonify it and send to angular

# I honestly know better, I shoukdnt have gone for 
# the hack solution but i foolishly did
