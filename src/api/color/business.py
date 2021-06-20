from src.database import db
from src.database.models import Color


def create_color(data):
    name = data.get('color')
    value = data.get('value')

    color = Color(name, value)

    db.session.add(color)
    db.session.commit()
