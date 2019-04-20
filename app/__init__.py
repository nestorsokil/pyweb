from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from app import auth

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:1234@127.0.0.1:3347/pyweb'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['SECRET_KEY'] = 'some-secret-string'
application.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
application.config['JWT_BLACKLIST_ENABLED'] = True
application.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

db = SQLAlchemy(application)
api = Api(application)
auth.init_jwt(application)
auth.init_api(api)

db.create_all()
