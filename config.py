import os


class Config(object):
    SECRET_KEY = os.environ.get('MY-SUPER-SECRET-KEY') or 'my-super-secret-key'