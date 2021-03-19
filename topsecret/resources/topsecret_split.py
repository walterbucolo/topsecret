from flask import Response
from flask_restful import (
    Resource,
    request, abort,
)
from flask_accepts import (
    accepts,
)

from topsecret.views.topsecret_view import TopSecretView
from topsecret.models.satellite import Satellite
from topsecret.schemas.satellite_schema import SatelliteSchema


class TopSecretSplit(Resource):
    satellites = []
    allowed_satellites = ["kenobi", "skywalker", "sato"]

    def get(self):
        if len(self.satellites) < 3:
            abort(404, error_message='Missing information')

        topsecret_response = TopSecretView().topsecret_view(self.satellites)

        return topsecret_response

    @accepts(schema=SatelliteSchema)
    def post(self, satellite_name):

        for saved_satellite in self.satellites:
            if satellite_name == saved_satellite.name:
                self.satellites.remove(saved_satellite)
        if satellite_name not in self.allowed_satellites:
            return abort(404, error_message='Unknown satellite name: {}'.format(satellite_name))

        data = request.json

        self.satellites.append(
            Satellite(
                name=satellite_name,
                distance=data["distance"],
                message=data["message"],
            )
        )
        return Response(status=201)
