import logging.config
from flask import Flask, Blueprint
from src.api.color.endpoints.colors import ns as colors_namespace
import os
from src import settings as settings
from src.database import db
from src.api.restx import api

logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '../logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)


def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    register_blueprints(app)
    initialize_extensions(app)
    return app


def initialize_extensions(app):
    db.init_app(app)


def register_blueprints(app):
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(colors_namespace)
    app.register_blueprint(blueprint)



