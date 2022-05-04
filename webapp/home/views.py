from flask import Blueprint, request, jsonify

from .schemas import QuestionSchema
from .utils import get_and_save_response
from webapp.quiz.models import QuizInfo

blueprint = Blueprint('home', __name__)   


@blueprint.route('/api', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num = request.form['questions_num']
        try:
            num = int(num)
            get_and_save_response(num)
            last_saved_question = QuizInfo.query.order_by(-QuizInfo.id).first()
            # last_saved_question = QuizInfo.query.get(100000000)
            question_schema = QuestionSchema()
            return question_schema.jsonify(last_saved_question), 200
        except ValueError:
            return 'Incorrect data type, must be integer instead', 400
