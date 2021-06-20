import logging.config
from flask import Flask, Blueprint
from src.api.color.endpoints.colors import ns as colors_namespace
import os
from src import settings as settings
from src.database import db
from src.api.restx import api

app = Flask(__name__)

logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '../logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)


def initialize_app(flask_app, config_filename='flask.cfg'):
    flask_app.config.from_pyfile(config_filename)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(colors_namespace)
    flask_app.register_blueprint(blueprint)

    db.init_app(flask_app)

    return flask_app


def main():
    initialize_app(app)
    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=settings.FLASK_DEBUG)


if __name__ == '__main__':
    main()
