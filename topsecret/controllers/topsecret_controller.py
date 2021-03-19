from flask import Response

from topsecret.services.location_service import GetLocation
from topsecret.services.message_service import GetMessage


class TopSecretController:

    allowed_satellites = ["kenobi", "skywalker", "sato"]

    def topsecret_controller(self, satellites):
        distances = {}
        messages = {}
        for satellite in satellites:
            if satellite.name not in self.allowed_satellites:
                return Response(status=404)
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
