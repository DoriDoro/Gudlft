"""create the fixtures (test_app and test_client) for the tests directory"""

import pytest

import server
from tests import mocks


@pytest.fixture
def test_app():
    t_app = server.app
    t_app.config["TESTING"] = True
    return t_app


@pytest.fixture
def test_client(test_app):
    with test_app.test_client() as test_client:
        yield test_client


@pytest.fixture
def mock_clubs_valid():
    server.clubs = mocks.mock_load_clubs_valid()


@pytest.fixture
def mock_clubs_invalid():
    server.clubs = mocks.mock_load_clubs_invalid()


@pytest.fixture
def mock_competitions_valid():
    server.competitions = mocks.mock_load_competition_valid()


@pytest.fixture
def mock_competitions_invalid():
    server.competitions = mocks.mock_load_competition_invalid()
