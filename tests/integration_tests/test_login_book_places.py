"""
This file test_login_book_places.py contains an integration test. It will test the login of one
secretary and one purchase of places of a competition.
- tests the login with pytest-mock
- tests the purchase of places of one competition
"""
from datetime import datetime

from tests.mocks import (
    mock_load_clubs_valid,
    mock_load_competition_valid,
    VALID_CLUB_EMAIL,
    VALID_COMPETITION_NAME,
    VALID_CLUB_NAME,
    VALID_CLUB_POINTS,
    INVALID_COMPETITION_NAME,
    INVALID_CLUB_NAME,
    VALID_COMPETITION_DATE,
    mock_load_competition_invalid,
)

PLACES_INPUT_VALID = 5
PLACES_INPUT_INVALID = 13
PURCHASE_PLACES_VALID = 6
PURCHASE_PLACES_INVALID = 15


def test_login_and_book_places(test_client, mock_clubs_valid, mock_competitions_valid):
    """
    GIVEN a Flask app for testing
    WHEN the urls: '/show-summary', '/book/<competition>/<club>', '/purchase-places'
        page is requested (GET and POST)
    THEN check if available points are correct in response
            use:
            - valid club
            - valid competition
            - 6 places
    """

    test_client.post("/show-summary", data={"email": VALID_CLUB_EMAIL})
    test_client.get(f"/book/{VALID_COMPETITION_NAME}/{VALID_CLUB_NAME}")
    response = test_client.post(
        "/purchase-places",
        data={
            "competition": VALID_COMPETITION_NAME,
            "club": VALID_CLUB_NAME,
            "places": PURCHASE_PLACES_VALID,
        },
    )
    assert response.status_code == 200
    result = int(VALID_CLUB_POINTS) - PURCHASE_PLACES_VALID
    assert f"Points available: {result}" in str(response.data)


def test_login_and_book_invalid_competition(
    test_client, mock_clubs_valid, mock_competitions_valid, mock_competitions_invalid
):
    """
    GIVEN a Flask app for testing
    WHEN the urls: '/show-summary', '/book/<competition>/<club>' page is requested (GET and POST)
    THEN check if error message is displayed:
        Sorry, but this competition is already over!
    """

    test_client.post("/show-summary", data={"email": VALID_CLUB_EMAIL})
    today = datetime.now().replace(microsecond=0)
    if VALID_COMPETITION_DATE < str(today):
        response = test_client.get(
            f"/book/{INVALID_COMPETITION_NAME}/{INVALID_CLUB_NAME}"
        )
        assert response.status_code == 200
        assert b"Sorry, but this competition is already over!" in response.data


def test_login_purchase_invalid_places_input(
    test_client, mock_clubs_valid, mock_competitions_valid
):
    """
    GIVEN a Flask app for testing
    WHEN the urls: '/show-summary', '/book/<competition>/<club>' and '/purchase-places'
        page is requested (GET and POST)
    THEN check if error message is displayed:
        You can not book more than 12 places!
            use:
            - valid club
            - valid competition
            - 15 places
    """

    test_client.post("/show-summary", data={"email": VALID_CLUB_EMAIL})
    test_client.get(f"/book/{VALID_COMPETITION_NAME}/{VALID_CLUB_NAME}")
    response = test_client.post(
        "/purchase-places",
        data={
            "competition": VALID_COMPETITION_NAME,
            "club": VALID_CLUB_NAME,
            "places": PURCHASE_PLACES_INVALID,
        },
    )
    assert response.status_code == 200
    assert b"You can not book more than 12 places!" in response.data
