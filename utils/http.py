from flask import make_response, jsonify
from functools import wraps


def returns_json(func):
    @wraps(func)
    def jsonify_response(*args, **kwargs):
        result, status = func(*args, **kwargs)
        return make_response(jsonify(result)), status
    return jsonify_response
