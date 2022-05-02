import requests

from webapp.quiz.models import QuizInfo

URL = 'https://jservice.io/api/random?count={num}'


def get_and_save_responce(questions_num):
    responce = requests.get(
        URL.format(num=questions_num)
    ).json()
    for question_info in responce:
        QuizInfo(
            id=question_info.get('id'),
            question=question_info.get('question'),
            answer=question_info.get('answer'),
            published=question_info.get('airdate')
        )
    