from marshmallow import fields, Schema


class SatelliteSchema(Schema):
    name = fields.String(attribute='name')
    distance = fields.Float(attribute='distance')
    message = fields.List(fields.String)


class SatellitesSchema(Schema):

    satellites = fields.List(fields.Nested(SatelliteSchema))
