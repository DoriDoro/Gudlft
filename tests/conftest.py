"""create the fixtures for the tests directory"""

import pytest

from server import app


@pytest.fixture
def test_app():
    t_app = app
    t_app.config["TESTING"] = True
    return t_app


@pytest.fixture(scope="module")
def clubs_fixture():
    """This fixture sets a fake list of clubs for the tests"""

    clubs = [
        {"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"},
        {"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"},
        {"name": "She Lifts", "email": "kate@shelifts.co.uk", "points": "12"},
    ]
    return clubs


@pytest.fixture(scope="module")
def competitions_fixture():
    """This fixture sets a fake list of competitions for the tests"""

    competitions = [
        {
            "name": "Spring Festival",
            "date": "2024-03-27 10:00:00",
            "number_of_places": "25",
        },
        {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "number_of_places": "13",
        },
    ]
    return competitions
