import os
from flaskext.mysql import MySQL


class Config(object):
    SECRET_KEY = 'you-will-never-guess'

    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'