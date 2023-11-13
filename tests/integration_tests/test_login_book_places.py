"""
This file test_login_book_places.py contains an integration test. It will test the login of one
secretary and one purchase of places of a competition.
- tests the login with pytest-mock
- tests the purchase of places of one competition
"""
from tests.mocks import (
    mock_load_clubs_valid,
    mock_load_competition_valid,
)
from tests.functional_tests.test_book import (
    test_book_valid_competition,
    test_book_invalid_competition,
)
from tests.functional_tests.test_purchase_places import test_purchase_places_successful
from tests.functional_tests.test_show_summary import test_show_summary_successful_login

PLACES_INPUT_VALID = 5
PLACES_INPUT_INVALID = 13


def test_login_and_book_places(mocker, test_client):
    mocker.patch("server.load_clubs", mock_load_clubs_valid)
    mocker.patch("server.load_competitions", mock_load_competition_valid)

    test_show_summary_successful_login(test_client)
    test_book_valid_competition(test_client)
    test_purchase_places_successful(test_client)


def test_login_and_book_invalid_competition(mocker, test_client):
    mocker.patch("server.load_clubs", mock_load_clubs_valid)
    mocker.patch("server.load_competitions", mock_load_competition_valid)

    test_show_summary_successful_login(test_client)
    test_book_invalid_competition(test_client)


def test_login_purchase_invalid_places_input(mocker, test_client):
    mocker.patch("server.load_clubs", mock_load_clubs_valid)
    mocker.patch("server.load_competitions", mock_load_competition_valid)

    test_show_summary_successful_login(test_client)
    test_book_valid_competition(test_client)
    test_purchase_places_successful(test_client)
