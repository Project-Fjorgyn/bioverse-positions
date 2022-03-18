from flask import Flask
from flask_restful import Api

from resources.location import Location, Locations

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['PROPOGATE_EXCEPTIONS'] = True
api = Api(app)

api.add_resource(Location, '/location')
api.add_resource(Locations, '/locations')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
