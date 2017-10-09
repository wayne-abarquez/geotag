# from .models import Geotag
# from app.utils import forms_helper
from app import app
from app.resources import UploadResource
import os
import gpsimage
import simplekml
import requests
import json
import logging

log = logging.getLogger(__name__)

UPLOAD_FOLDER = app.config['UPLOAD_FOLDER']
KMZ_PATH = app.config['KMZ_PATH']


def get_location_by_geolocation_api():
    url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=' + app.config.get('GOOGLE_MAP_API_KEY')
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps({'considerIp': 'true'}), verify=False, headers=headers)
    if response.content:
        content = response.json()
        # log.debug("geolocation api response: {0}".format(content))
        return {
            'lat': content['location']['lat'],
            'lng': content['location']['lng']
        }

    return None


def process_geotag(file, caption):
    upload = UploadResource()
    filename = upload.copy_file(file)
    pic_filepath = os.path.join(UPLOAD_FOLDER, filename)

    img_data = gpsimage.open(pic_filepath)
    img_data_json = img_data.json
    # log.debug('img data JSON: {0}'.format(img_data_json))
    # log.debug('img data: {0}'.format(img_data))

    if img_data_json['status'] == 'OK':
        latlng = {
            'lat': img_data.lat,
            'lng': img_data.lng
        }
    else:
        latlng = get_location_by_geolocation_api()
        log.debug("GEOLOCATION LATLNG: {0}".format(latlng))
        if latlng is None:
            return False

    # log.debug("LATLNG: {0}".format(latlng))

    kml = simplekml.Kml(name=caption)
    kml_picpath = kml.addfile(pic_filepath)

    point = kml.newpoint(name=caption, coords=[(latlng['lng'], latlng['lat'])])
    point.description = '<img src="' + kml_picpath + '" width="400" />'

    point.style.labelstyle.color = simplekml.Color.red  # Make the text red
    point.style.labelstyle.scale = 2
    point.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/pal2/icon13.png'

    # kmz_filename = filename.rsplit('.', 1)[0].lower() + '.kmz'
    kmz_filename = 'geotag.kmz'

    kmz_filepath = os.path.join(KMZ_PATH, kmz_filename)
    kml.savekmz(kmz_filepath, format=False)

    return {
        'latlng': latlng,
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
