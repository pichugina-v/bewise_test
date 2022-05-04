
from urllib import response
from flask import Blueprint, request, render_template, jsonify

from .schemas import QuestionSchema
from .utils import get_and_save_response
from webapp.quiz.models import QuizInfo

blueprint = Blueprint('home', __name__)   
   
@blueprint.route('/api', methods=['GET', 'POST'])
def index():
    # title = 'Quiz questions'
    # form = QuestionNumForm()
    # if request.method == 'POST':
    #     if form.validate_on_submit():
    #         num = form.number.data
    #         print(num)
    #         get_and_save_response(num)
    #         title = 'Question'
    #         last_saved_question = QuizInfo.query.order_by(-QuizInfo.id).first()
    #         # last_saved_question = QuizInfo.query.get(1000)
    #         print(last_saved_question)
    #         return render_template(
    #             'questions/question.html',
    #             page_title=title,
    #             question=last_saved_question)
    # return render_template(
    #     'home/index.html',
    #     page_title=title,
    #     form=form)
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
            return 'Incorrect data type, must be integer', 400
