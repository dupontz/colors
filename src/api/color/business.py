from src.database import db
from src.database.models import Color


def create_color(data):
    name = data.get('name')
    color_id = data.get('id')

    color = Color(name)
    if color_id:
        color.id = color_id

    db.session.add(color)
    db.session.commit()
