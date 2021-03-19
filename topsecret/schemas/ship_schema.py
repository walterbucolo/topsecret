from marshmallow import fields, Schema


class ShipSchema(Schema):
    position = fields.Dict(keys=fields.Str(), values=fields.Float())
    message = fields.String(attribute='message')
