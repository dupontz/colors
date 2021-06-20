from flask_restx import fields
from src.api.restx import api

color = api.model('Color', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a color'),
    'name': fields.String(required=True, description='Category name'),
    # 'value': fields.String(required=True, description='Category name'),
})
