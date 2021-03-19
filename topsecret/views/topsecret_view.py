from flask import Response
from flask_restful import abort

from topsecret.services.location_service import GetLocation
from topsecret.services.message_service import GetMessage


class TopSecretView:

    def topsecret_view(self, satellites):
        distances = {}
        messages = {}
        for satellite in satellites:
            distances[satellite.name] = satellite.distance
            messages[satellite.name] = satellite.message

        x, y = GetLocation().get_location(distances["kenobi"], distances["skywalker"], distances["sato"])
        message = GetMessage().get_message(messages["kenobi"], messages["skywalker"], messages["sato"])

        return {
            "position": {
                "x": x,
                "y": y,
            },
            "message": message
        }
