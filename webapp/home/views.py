
from flask import Blueprint, request, render_template

from .utils import get_and_save_responce

blueprint = Blueprint('home', __name__)   
   
@blueprint.route('/', methods=['GET', 'POST'])
def index():
    title = 'Quiz questions'
    if request.method == 'POST':
        questions_num = request.form['questions_num']
        if questions_num.isnumeric:
            get_and_save_responce(questions_num)
            return render_template('home/index.html', page_title=title)
    return render_template('home/index.html', page_title=title)
