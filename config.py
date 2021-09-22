import os

from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://olive:behanna2@localhost/pitchy')

class Config:
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://olive:behanna2@localhost/pitchy' 