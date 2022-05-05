from flask import Blueprint, request
from typing import Tuple, Union

from .models import QuizInfo
from .schemas import QuestionSchema
from .utils import get_and_save_response

blueprint = Blueprint('home', __name__)


@blueprint.route('/api', methods=['POST'])
def index() -> Tuple[str, int]:
    num: Union[int, str]
    
    num = request.form['questions_num']
    try:
        num = int(num)
        last_saved_question = QuizInfo.query.order_by(-QuizInfo.id).first()
        get_and_save_response(num)
        return QuestionSchema().jsonify(last_saved_question), 200
    except ValueError:
        return 'Incorrect data type, must be integer instead', 400
