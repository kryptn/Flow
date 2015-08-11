from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore
from flask.ext.social import Social, SQLAlchemyConnectionDatastore

app = Flask(__name__)

from flow.config import config_app

config_app(app, 'development')

db = SQLAlchemy(app)

import flow.views
import flow.models
