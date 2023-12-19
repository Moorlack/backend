from marshmallow import Schema, fields, validate


class CreateRecordSchema(Schema):
    user_id = fields.Integer(required=True)
    category_id = fields.Integer(required=True)
    sum = fields.Integer(required=True, validate=validate.Range(min=0, max=9999))


class RecordSchema(Schema):
    id = fields.Integer(required=True)
    sum = fields.Integer(required=True)
    user_id = fields.String()
    category_id = fields.String()
