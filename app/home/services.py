from .models import Geotag
from app.utils import forms_helper
from app import app, db
from app.resources import UploadResource
import os
import gpsimage
import simplekml
import logging

log = logging.getLogger(__name__)

UPLOAD_FOLDER = app.config['UPLOAD_FOLDER']
KMZ_PATH = app.config['KMZ_PATH']


def process_geotag(file, caption):
    upload = UploadResource()
    filename = upload.copy_file(file)
    pic_filepath = os.path.join(UPLOAD_FOLDER, filename)

    img_data = gpsimage.open(pic_filepath)

    kml = simplekml.Kml(name=caption)
    kml_picpath = kml.addfile(pic_filepath)

    point = kml.newpoint(name=caption, coords=[(img_data.lng, img_data.lat)])

    style = simplekml.Style()  # creates shared style for all points
    style.iconstyle.color = 'ffff00ff'  # magenta
    style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/pal2/icon13.png'
    style.iconstyle.scale = 1
    point.style = style

    point.description = '<img src="' + kml_picpath + '" width="400" height="300" align="left" />'

    # point.style.labelstyle.color = simplekml.Color.red  # Make the text red
    # point.style.labelstyle.scale = 2
    # point.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/pal2/icon13.png'

    # kmz_filename = filename.rsplit('.', 1)[0].lower() + '.kmz'
    kmz_filename = 'geotag.kmz'

    kmz_filepath = os.path.join(KMZ_PATH, kmz_filename)
    kml.savekmz(kmz_filepath, format=False)

    return {
        'latlng': {
            'lat': img_data.lat,
            'lng': img_data.lng
        },
        'filename': kmz_filename,
        'filepath': kmz_filepath
    }


def new_geotag(file, data):
    # Prepare Data
    # model = Geotag(caption=data['caption'])
    geotag_dict = process_geotag(file, data['caption'])

    # model.filename = geotag_dict['filename']
    # model.coordinates = forms_helper.parse_coordinates(geotag_dict['latlng'])

    # Persist
    # db.session.add(model)
    # db.session.commit()

    return geotag_dict
