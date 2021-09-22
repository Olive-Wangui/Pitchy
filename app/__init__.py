from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://olive:behanna2@localhost/pitchy' 
    
    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    
    return app