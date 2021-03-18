from flask_restful import Resource

from topsecret.services.location_service import GetLocation
from topsecret.services.message_service import GetMessage


class TopSecret(Resource):
    def post(self):
        data = {
            "satellites": [
                {
                    "name": "kenobi",
                    "distance": 4,
                    "message": ["este", " ", " ", "mensaje", " "],
                },
                {
                    "name": "skywalker",
                    "distance": 5.657,
                    "message": [" ", "es", " ", " ", "secreto"],
                },
                {
                    "name": "sato",
                    "distance": 4,
                    "message": ["este", " ", "un", " ", " "],
                },
            ]
        }

        distances = {}
        messages = {}
        for satellite in data['satellites']:
            distances[satellite['name']] = satellite['distance'] 
            messages[satellite['name']] = satellite['message']

        location = GetLocation()
        x, y = location.get_location(distances["kenobi"], distances["skywalker"], distances["sato"])
        message = GetMessage().get_message(messages["kenobi"], messages["skywalker"], messages["sato"])

        return {
            "position": {
                "x": x,
                "y": y,
            },
            "message": message
        }