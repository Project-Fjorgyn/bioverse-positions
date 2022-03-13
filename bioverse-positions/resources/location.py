from flask_restful import Resource, reqparser

from models.location import LocationModel

class Location(Resource):
    parser = reqparser.RequestParser()
    parser.add_argument(
        'hex_id'
        type=str,
        required=True,
        help='h3 hex id'
    )
    parser.add_argument(
        'zoom'
        type=int,
        required=True,
        help='h3 zoom level'
    )
    parser.add_argument(
        'genus'
        type=str,
        required=True,
        help='genus of the species'
    )
    parser.add_argument(
        'species'
        type=str,
        required=True,
        help='species name'
    )

    insert_parser = parser.copy()
    insert_parser.add_argument(
        'count'
        type=int,
        required=True,
        help='occurences'
    )

    def get(self):
        kwargs = Location.parser.parse_args()
        location = LocationModel.get_location(**kwargs)
        if location:
            return location.json()
        return {'message': 'Location not found'}, 404

    def delete(self):
        kwargs = Location.parser.parse_args()
        location = LocationModel.get_location(**kwargs)
        if location:
            location.delete_from_db()
            return {'message': 'Location deleted'}
        return {'message': 'Location not found'}, 404

    def put(self):
        kwargs = Location.insert_parser.parse_args()
        location = LocationModel.get_location(**kwargs)

        if location:
            location.count = kwargs['count']
        else:
            location = LocationModel(**kwargs)

        try:
            location.save_to_db()
        except:
            return {'message': 'Error occurred during insert'}, 500

        return location.json(), 201

    def post(self):
        kwargs = Location.insert_parser.parse_args()
        if LocationModel.get_location(**kwargs):
            return {'message': 'Location already inserted'}, 400
        location = LocationModel(**kwargs)

        try:
            location.save_to_db()
        except:
            return {'message': 'Error occurred during insert'}, 500

        return location.json(), 201
