from db import db

class LocationModel(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    hex_id = db.Column(db.String(15))
    species = db.Column(db.String(100))
    genus = db.Column(db.String(100))
    count = db.Column(db.Integer)

    def __init__(self, hex_id, genus, species, count):
        self.hex_id = hex_id
        self.genus = genus
        self.species = species
        self.count = count

    def json(self):
        return {
            'hex_id': self.hex_id,
            'genus': self.genus,
            'species': self.species,
            'count': self.count
        }

    @classmethod
    def get_location(cls, hex_id, genus, species, **kwargs):
        return cls.query.filter_by(
            hex_id=hex_id, genus=genus, species=species
        ).first()

    @classmethod
    def get_locations(cls, hex_ids, genus, species, **kwargs):
        return cls.query.filter_by(
            species=species, genus=genus,
        ).filter(cls.hex_id.in_(hex_ids)).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()