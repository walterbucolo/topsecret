
from flask_restful import (
    Resource,
    request,
)

from topsecret.controllers.topsecret_controller import TopSecretController
from topsecret.models.satellite import Satellite


class TopSecret(Resource):

    def post(self):
        satellites = []
        data = request.json
        for satellite in data["satellites"]:
            satellites.append(
                Satellite(
                    name=satellite["name"],
                    distance=satellite["distance"],
                    message=satellite["message"],
                )
            )

        top_secret_response = TopSecretController().topsecret_controller(satellites)

        return top_secret_response
