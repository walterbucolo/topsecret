

class GetLocation:
    """
    This class calculates the location (x, y) of the ship from the distances and location of the satellites.
    """

    satellite_location = {
        'kenobi': [-500, -200],
        'skywalker': [100, -100],
        'sato': [500, 100],
    }

    def get_location(self, kenobi_distance, skywalker_distance, sato_distance):

        x1 = self.satellite_location['kenobi'][0]
        x2 = self.satellite_location['skywalker'][0]
        x3 = self.satellite_location['sato'][0]
        y1 = self.satellite_location['kenobi'][1]
        y2 = self.satellite_location['skywalker'][1]
        y3 = self.satellite_location['sato'][1]

        a = -2*x1 + 2*x2
        b = -2*y1 + 2*y2
        c = pow(kenobi_distance, 2) - pow(skywalker_distance, 2) - pow(x1, 2) + pow(x2, 2) - pow(y1, 2) + pow(y2, 2)
        d = -2*x2 + 2*x3
        e = -2*y2 + 2*y3
        f = pow(skywalker_distance, 2) - pow(sato_distance, 2) - pow(x2, 2) + pow(x3, 2) - pow(y2, 2) + pow(y3, 2)

        x = (c*e-f*b) / (e*a-b*d)
        y = (c*d-a*f) / (b*d-a*e)

        return round(x, 1), round(y, 1)
