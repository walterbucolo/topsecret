
from flask_restful import (
    Resource,
    request,
)

from topsecret.services.location_service import GetLocation
from topsecret.services.message_service import GetMessage


class TopSecret(Resource):

    def post(self):

        data = request.json
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
