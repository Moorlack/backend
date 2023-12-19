from marshmallow import Schema, fields, validate


class CategoryCreateSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=3, max=80))


class CategorySchema(Schema):
    name = fields.Str(required=True)
    id = fields.Integer(required=True)


class AddApprovedUser(Schema):
    user_id = fields.Integer(required=True)
    category_id = fields.Integer(required=True)
