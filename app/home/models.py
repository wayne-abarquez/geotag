from app import db
from app.models import BaseModel
from geoalchemy2 import Geometry


class Geotag(BaseModel):
    caption = db.Column(db.Text)
    filename = db.Column(db.String(200), nullable=False)
    coordinates = db.Column(Geometry('POINT'), nullable=False)

# class SolarFile(BaseModel):
#     solar_id = db.Column(db.Integer, db.ForeignKey('solar.id'), nullable=False)
#     caption = db.Column(db.Text)
#     file_name = db.Column(db.Text, nullable=False)
#     type = db.Column(db.Text, nullable=False)
#     solar = db.relationship(Solar, backref='files')
#
#     def __init__(self, *args, **kwargs):
#         super(SolarFile, self).__init__(*args, **kwargs)
#         self.src = self.get_url()
#         print '__init__ is called from solarfile'
#
#     # def __get__(self, instance, owner):
#     # print '__get__ from solarFile called'
#     #     if instance is None:
#     #         return None
#     #
#     #     instance.src = self.get_url()
#     #     return super(SolarFile, self).__get__(instance, owner)
#
#     def get_url(self):
#         return url_for('static', _external=True, filename='uploads/' + self.file_name)
