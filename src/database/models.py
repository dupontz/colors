from src.database import db
import json


class Color(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(50))
    value = db.Column(db.String(4))

    def __init__(self, name, value):
        self.color = name
        self.value = value

    def __repr__(self):
        return '<Color %r>' % self.name


@db.event.listens_for(Color.__table__, 'after_create')
def populate_colors(*args, **kwargs):
    with open("colors.json", "r") as f:  # open the unmodified `tag.tg`
        json_data = json.load(f)  # parse its JSON

    for entry in json_data:  # iterate over each entry in the `tag.tg`
        db.session.add(Color(entry['color'], entry['value']))  # insert it in the DB
    db.session.commit()
