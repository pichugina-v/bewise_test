from webapp.ma import ma
from .models import QuizInfo


class QuestionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = QuizInfo
        fields = ('question', )
