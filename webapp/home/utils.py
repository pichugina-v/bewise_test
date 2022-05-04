import requests
from datetime import datetime as dt

from webapp.quiz.models import QuizInfo
from webapp.db import db

URL = 'https://jservice.io/api/random?count={num}'


def get_and_save_response(questions_num):
    response = requests.get(
        URL.format(num=questions_num)
    ).json()
    for question_info in response:
        print(len(response))
        if bool(QuizInfo.query.filter_by(
            question=question_info.get('question')
        ).first()) == False:
            new_question_info = QuizInfo(
                question_info.get('id'),
                question_info.get('question'),
                question_info.get('answer'),
                dt.strptime(
                    question_info.get('airdate'),
                    '%Y-%m-%dT%H:%M:%S.%fZ'
                )
            )
            db.session.add(new_question_info)
            db.session.commit()
        else:
            response.append(requests.get(
                URL.format(num=1)
            ).json()[0])

    