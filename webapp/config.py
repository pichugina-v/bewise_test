import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql:///quiz'

SECRET_KEY = 'VERY_SECRET_KEY'
