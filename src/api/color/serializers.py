from flask_restx import fields
from src.api.restx import api

color = api.model('Color', {
    'color': fields.String(required=True, description='Color name'),
    'value': fields.String(required=True, description='Color hex value'),
})
