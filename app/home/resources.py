from flask.ext.restful import Resource, abort, marshal
from flask import request, send_from_directory
from app import app, rest_api
from app.resources import UploadResource
from .services import new_geotag
from .fields import geotag_create_fields, geotag_raw_fields
import logging

KMZ_PATH = app.config['KMZ_PATH']

log = logging.getLogger(__name__)


class GeotagFileResource(UploadResource):
    """
    Resource for upload goetag photos/files
    """

    def post(self):
        data = request.form

        log.debug("POST Geotag Upload Photo request : {0}".format(data))

        uploaded_file = request.files['file']

        if uploaded_file and self.allowed_file(uploaded_file.filename):
            result_dict = new_geotag(uploaded_file, data)
            return request.url_root + 'static/kmz/' + result_dict['filename']
            # return send_from_directory(KMZ_PATH, result_dict['filename'], as_attachment=True, mimetype="application/vnd.google-earth.kmz")
            # resp = Response(
            #     file,
            #     mimetype="application/vnd.google-earth.kmz",
            #     headers={"Content-disposition": "attachment; filename=" + result_dict['filename']}
            # )
            # return resp
            # result = dict(geotag=resp)
            # return marshal(result, geotag_raw_fields)
        else:
            abort(400, message="Invalid parameters")


rest_api.add_resource(GeotagFileResource, '/api/geotags/upload')
