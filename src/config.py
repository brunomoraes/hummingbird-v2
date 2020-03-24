import os
basedir = os.path.abspath(os.path.dirname(__file__))


class DefaultConfig(object):
    DEBUG = True
    TESTING = False
    BUNDLE_ERRORS = True
    PROPAGATE_EXCEPTIONS = True

    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(DefaultConfig):
    TESTING = False
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://teste:teste@db:5432/hummingbird-v2'


class TestingConfig(DefaultConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test_data/test.db')


class StagingConfig(DefaultConfig):
    TESTING = False


class ProductionConfig(DefaultConfig):
    TESTING = False
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://teste:teste@127.0.0.1:54320/hummingbird-v2"


default = DefaultConfig()
development = DevelopmentConfig()
testing = TestingConfig()
staging = StagingConfig()
production = ProductionConfig()
