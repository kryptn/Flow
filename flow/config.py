from flow.secret_config import DevelopmentConfig

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    # sqlite :memory: identifier is the default if no filepath is present
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

config = {
    "development": "flow.config.DevelopmentConfig",
    "testing": "flow.config.TestingConfig",
    "default": "flow.config.DevelopmentConfig"
}

def config_app(app, config_name):
    app.config.from_object(config[config_name])