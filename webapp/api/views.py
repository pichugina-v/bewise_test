from flask import Blueprint, request
from typing import Dict, Tuple, Union

from .models import QuizInfo
from .schemas import QuestionSchema
from .utils import get_and_save_response

blueprint = Blueprint('home', __name__)

ZERO_VALUE_ERROR = "Value must be greater than 0"
DATA_TYPE_ERROR = "Incorrect data type, must be integer instead"


@blueprint.route('/api', methods=['POST'])
def index() -> Union[Tuple[str, int], Tuple[Dict[str, str], int]]:
    num: Union[int, str]

    num = request.form['questions_num']
    try:
        num = int(num)
        if num == 0:
            return {"error_message": ZERO_VALUE_ERROR}, 400
        last_saved_question = QuizInfo.query.order_by(-QuizInfo.id).first()
        get_and_save_response(num)
        return QuestionSchema().jsonify(last_saved_question), 200
    except ValueError:
        return {"error_message": DATA_TYPE_ERROR}, 400
