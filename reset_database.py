from src.app import initialize_app, app
from src.database import reset_database

initialize_app(app)
with app.app_context():
    reset_database()
