import os

class Config:
    """ basic configurations. """
    DEBUG = False
    PORT = os.environ.get('PORT') or 5000
    ENV = os.environ.get('ENV')

class development(Config):
    """ development configurations """
    DEBUG = True

class production(Config):
    """ production configurations """

    PORT = os.environ.get('PORT') or 8080
