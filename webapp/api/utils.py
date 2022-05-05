import datetime
import requests
from datetime import datetime as dt
from typing import Callable, Dict, List, Union

from webapp.db import db
from .models import QuizInfo

URL = 'https://jservice.io/api/random?count={num}'


def get_and_save_response(questions_num: int) -> None:
    response: List
    question_info: Dict[str, Union[int, str]]
    
    response = requests.get(
        URL.format(num=questions_num)
    ).json()
    print(response)
    for question_info in response:
        if not bool(QuizInfo.query.filter_by(
            question=question_info.get('question')
        ).first()):
            new_question_info = QuizInfo(
                question_info.get('id'),
                question_info.get('question'),
                question_info.get('answer'),
                dt.strptime(
                    str(question_info.get('airdate')),
                    '%Y-%m-%dT%H:%M:%S.%fZ'
                )
            )
            db.session.add(new_question_info)
            db.session.commit()
        else:
            response.append(requests.get(
                URL.format(num=1)
            ).json()[0])
