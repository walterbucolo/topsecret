from flask_accepts import accepts, responds
from flask_restful import (
    Resource,
    request,
)

from topsecret.views.topsecret_view import TopSecretView
from topsecret.models.satellite import Satellite
from topsecret.schemas.satellite_schema import SatellitesSchema
from topsecret.schemas.ship_schema import ShipSchema


class TopSecret(Resource):

    @accepts(schema=SatellitesSchema)
    @responds(schema=ShipSchema)
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

        top_secret_response = TopSecretView().topsecret_view(satellites)

        return top_secret_response
