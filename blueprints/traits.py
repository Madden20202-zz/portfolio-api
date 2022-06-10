from flask import jsonify
from flask import Blueprint

# information needed: characteristics, positive habits, hobbies

characteristics = {
    'Smart',
    'Responsive',
    'Understanding',
    'Empathetic',
    'Hard Working',
    'Loyal'
}

positive_habits = {
    'Workout',
    'Constant Studying',
    'Book a Week'
}

traits_bp = Blueprint('traits', __name__)

@traits_bp.route('/')

def give_traits():
    return jsonify({
        'characteristics': characteristics
    })