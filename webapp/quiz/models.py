from enum import unique
from webapp.db import db

class QuizInfo(db.Model):
    def __init__(self, question_id, question, answer, published):
        self.question_id = question_id
        self.question = question
        self.answer = answer
        self.published = published

    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, unique=True)
    question = db.Column(db.String, nullable=False, unique=True)
    answer = db.Column(db.String, nullable=False)
    published = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Question {} {}>'.format(self.question_id, self.question)