from enum import unique
from webapp.db import db

class QuizInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, unique=True)
    question = db.Column(db.String, nullable=False)
    answer = db.Column(db.String, nullable=False)
    published = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Question {} {}>'.format(self.question_id, self.question)