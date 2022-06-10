from flask import jsonify
from flask import Blueprint

personal_info_bp = Blueprint('personal', __name__)

@personal_info_bp.route('/')

def give_personal_info():
    return jsonify{{
        'name': 'Austin Martz',
        'address': '407 W 6th Street Okmulgee OK 74447',
        'phone_number': '539-286-3763',
        'github_page': 'github.com/madden20202'
    }}