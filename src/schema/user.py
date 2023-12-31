from marshmallow import Schema, fields, validate


class CreateUserSchema(Schema):
    name = fields.Str(
        required=True,
        validate=validate.Length(min=3, max=30),
    )
    password = fields.Str(
        required=True,
        validate=validate.Length(min=3, max=100)
    )


class UserSchema(Schema):
    name = fields.Str(required=True)
    id = fields.Int(required=True)
