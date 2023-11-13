"""create the fixtures for the tests directory"""

import pytest

from server import app


@pytest.fixture
def test_app():
    t_app = app
    t_app.config["TESTING"] = True
    return t_app


@pytest.fixture
def test_client(test_app):
    with test_app.test_client() as test_client:
        yield test_client
