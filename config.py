import os

class Config(object):
    # the SECRET_KEY config var is a very important part of most flask apps
    # Flask-WTF uses it to protext its web forms from CSRF attacks
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'