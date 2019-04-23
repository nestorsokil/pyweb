from application import app
from utils.http import returns_json


@app.errorhandler(Exception)
@returns_json
def handle_generic_exception(exc):
    # todo log
    return {'message':'Internal Server Error'}, 500
