import os

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
