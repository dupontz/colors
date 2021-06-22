from src import create_app
from src.database import reset_database

app = create_app('flask.cfg')
with app.app_context():
    reset_database()
