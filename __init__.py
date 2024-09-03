from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
db=SQLAlchemy()
DB_NAME="database.db"

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='S5LA'
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_NAME}'
    db.init_app(app)
    from .views import view
   
    from .auth import auths
    app.register_blueprint(view,url_prefix='/')
    app.register_blueprint(auths,url_prefix='/')
    from .models import User, Note

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')