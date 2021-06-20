import logging

from flask import request
from flask_restx import Resource
from src.api.color.business import create_color
from src.api.color.serializers import color
from src.api.restx import api
from src.database.models import Color

log = logging.getLogger(__name__)

ns = api.namespace('color', description='Operations related to color')


@ns.route('/')
class ColorCollection(Resource):

    @api.marshal_list_with(color)
    def get(self):
        """
        Returns list of colors.
        """

        colors = Color.query.all()
        return colors

    @api.response(201, 'Color successfully created.')
    @api.expect(color)
    def post(self):
        """
        Creates a new color entry.
        """
        data = request.json
        create_color(data)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Color not found.')
class ColorItem(Resource):

    @api.marshal_with(color)
    def get(self, id):
        """
        Returns a color.
        """
        return Color.query.filter(Color.id == id).one()
