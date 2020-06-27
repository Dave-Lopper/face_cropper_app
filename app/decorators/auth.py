import os

from flask import request


def auth_decorator(function):
    """Performs the auth by checking on the x-api-key request header.

    Args:
        function [function]: the function (blueprint endpoint) to be checked
    """
    def wrapper(*args, **kwargs):
        print("RAN")
        key = request.headers.get('x-api-key')
        if key is None:
            return ("No API key provided", 401)
            print("TOTO")
        if key != os.environ["API_KEY"]:
            return ("Bad API key provided", 401)
        return function(*args, **kwargs)
    wrapper.__name__ = function.__name__
    return wrapper
