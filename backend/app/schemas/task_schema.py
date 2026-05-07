from marshmallow import Schema, fields, validate


class CreateTaskSchema(Schema):
    title = fields.String(
        required=True,
        validate=validate.Length(min=3, max=255),
    )

    description = fields.String(required=False)

    priority = fields.String(
        required=True,
        validate=validate.OneOf(
            ["LOW", "MEDIUM", "HIGH"]
        ),
    )


class TransitionTaskSchema(Schema):
    to_status = fields.String(required=True)