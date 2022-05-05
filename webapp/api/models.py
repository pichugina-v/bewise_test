from datetime import datetime
from webapp.db import db


class QuizInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, unique=True)
    question = db.Column(db.String, nullable=False, unique=True)
    answer = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, nullable=False)

    def __init__(self, question_id, question, answer, created) -> None:
        self.question_id = question_id
        self.question = question
        self.answer = answer
        self.created = created

    def __repr__(self) -> str:
        return '<Id {}: Question {}>'.format(self.question_id, self.question)
