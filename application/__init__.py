from flask import Flask
from application.shared.database import db
from application.jwt import jwt
from application.auth.v1_controller import auth_v1
from application.http import httperrors
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:1234@127.0.0.1:3347/pyweb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'some-secret-string'
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

db.app = app
db.init_app(app)
db.create_all()

jwt.init_app(app)

app.register_blueprint(auth_v1)
app.register_blueprint(httperrors)
# ...
