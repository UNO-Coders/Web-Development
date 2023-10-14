"""Request schemas for the API endpoints."""

from marshmallow import Schema, fields, validate, INCLUDE


class SnapshotBaseSchema(Schema):
    """Schema to validate the snapper request."""
    class Meta:
        unknown = INCLUDE

    page_width = fields.Integer(required=True, validate=validate.Range(min=1))
    page_height = fields.Integer(required=True, validate=validate.Range(min=1))
    full_page = fields.Boolean(required=False, load_default=False)
    attachment = fields.Boolean(required=False, load_default=False)


class SnapshotURLSchema(SnapshotBaseSchema):
    """Schema to snapshot URL content"""
    class Meta:
        unknown = INCLUDE

    page_url = fields.Url(required=True, validate=validate.URL(schemes=["http", "https"]))


class SnapshotHTMLSchema(SnapshotBaseSchema):
    """Schema to snapshot HTML content"""
    class Meta:
        unknown = INCLUDE

    page_content = fields.String(required=True)


class SnapshotMultipleSchema(Schema):
    """Schema to validate the snapper request."""
    class Meta:
        unknown = INCLUDE

    pages = fields.List(fields.Nested(SnapshotHTMLSchema), required=True)
