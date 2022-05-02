
from flask import Flask
from flask_migrate import Migrate

from webapp.db import db
from webapp.quiz.models import QuizInfo
from webapp.home.views import blueprint as home_blueprint



def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_pyfile('config.py') 
    db.init_app(app)
    migrate = Migrate(app, db, render_as_batch=True)  

    app.register_blueprint(home_blueprint)

    return app

app = create_app()
