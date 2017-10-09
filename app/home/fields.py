from flask.ext.restful import fields
from app.utils.gis_json_fields import PointToLatLng

success_fields = dict(
    status=fields.String,
    message=fields.String,
)

geotag_fields = dict(
    id=fields.Integer,
    caption=fields.String,
    filename=fields.String,
    coordinates=PointToLatLng(attribute='coordinates'),
    date_created=fields.DateTime("iso8601"),
    date_modified=fields.DateTime("iso8601")
)

geotag_create_fields = dict(
    status=fields.String,
    message=fields.String,
    geotag=fields.Nested(geotag_fields, allow_null=False)
)

geotag_raw_fields = dict(
    geotag=fields.Raw
)
