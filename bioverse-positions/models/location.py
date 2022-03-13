from db import db

class LocationModel(db.Model):
    __tablename__ = 'locations'

    hex_id = db.Column(db.String(15))
    zoom = db.Column(db.Integer)
    species = db.Column(db.String(100))
    genus = db.Column(db.String(100))
    count = db.Column(db.Integer)

    def __init__(self, hex_id, zoom, genus, species, count):
        self.hex_id = hex_id
        self.zoom = zoom
        self.genus = genus
        self.species = species
        self.count = count

    def json(self):
        return {
            'hex_id': self.hex_id,
            'zoom': self.zoom,
            'genus': self.genus,
            'species': self.species,
            'count': self.count
        }

    @classmethod
    def get_location(cls, hex_id, zoom, genus, species):
        return cls.query.filter_by(
            hex_id=hex_id, zoom=zoom, genus=genus, species=species
        ).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()