from flask import Flask
from application.shared.database import db
from application.jwt import jwt
from application.auth.v1_controller import auth_v1
from application.http import httperrors
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config.from_object('config')

db.app = app
db.init_app(app)
db.create_all()

jwt.init_app(app)

app.register_blueprint(auth_v1)
app.register_blueprint(httperrors)
# ...
