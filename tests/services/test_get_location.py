
from topsecret.services.location_service import GetLocation


def test_it_should_return_the_location():
    location = GetLocation()
    location.satellite_location = {
        'kenobi': [-2, 2],
        'skywalker': [2, 2],
        'sato': [2, -2],
    }
    x, y = location.get_location(kenobi_distance=4, skywalker_distance=5.657, sato_distance=4)

    assert x == -2.0
    assert y == -2.0
