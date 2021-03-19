from flask import Response
from flask_restful import (
    Resource,
    request,
)
from flask_accepts import (
    accepts,
    responds,
)

from topsecret.controllers.topsecret_controller import TopSecretController
from topsecret.models.satellite import Satellite
from topsecret.schemas.satellite_schema import SatelliteSchema


class TopSecretSplit(Resource):
    satellites = []

    def get(self):
        if len(self.satellites) < 3:
            Response(status=404)

        topsecret_response = TopSecretController().topsecret_controller(self.satellites)

        return topsecret_response

    @accepts(schema=SatelliteSchema)
    def post(self, satellite_name):

        for saved_satellite in self.satellites:
            if satellite_name == saved_satellite.name:
                self.satellites.remove(saved_satellite)

        data = request.json

        self.satellites.append(
            Satellite(
                name=satellite_name,
                distance=data["distance"],
                message=data["message"],
            )
        )
        return Response(status=200)
