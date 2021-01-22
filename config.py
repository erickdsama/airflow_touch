import datetime
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # clave mamona
    # MAIL CONF
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    # JWT CONF
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET')
    JWT_ALGORITHM = os.environ.get('JWT_SECRET', "RS256")
    # JWT_PUBLIC_KEY = open('./id_rsa.pub').read()
    # JWT_PRIVATE_KEY = open('./id_rsa').read()
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=1)
    # DATABASE
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=15)
    SQLALCHEMY_DATABASE_URI = "postgresql://project@psql/project"

class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=7)
    SQLALCHEMY_DATABASE_URI = "postgresql://project@psql/project"

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
