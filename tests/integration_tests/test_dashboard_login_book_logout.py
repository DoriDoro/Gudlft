"""
This file test_dashboard_login_book_logout.py contains an integration test. It will test to go to
dashboard, login of one secretary, purchase of places of a valid competition and logout.
- tests the login with pytest-mock
- tests the purchase of places of one competition
"""
from datetime import datetime
from flask import url_for

from Python_Testing.tests.mocks import (
    VALID_CLUB_NAME,
    VALID_CLUB_EMAIL,
    VALID_CLUB_POINTS,
    INVALID_CLUB_NAME,
    INVALID_CLUB_POINTS,
    VALID_COMPETITION_NAME,
    INVALID_COMPETITION_NAME,
    INVALID_COMPETITION_DATE,
)

PURCHASE_PLACES = 6


def test_dashboard_login_book_logout(
    test_client, mock_clubs_valid, mock_competitions_valid
):
    """
    GIVEN a Flask app for testing
    WHEN the urls: '/dashboard', '/', '/show-summary', '/book/<competition>/<club>',
        '/purchase-places' and '/logout' pages are requested (GET and POST)
    THEN check if available points are correct in response and
        if the redirect to the home page is working
            use:
            - valid club
            - valid competition
            - 6 places
    """

    test_client.get("/dashboard")
    test_client.get("/")
    test_client.post("/show-summary", data={"email": VALID_CLUB_EMAIL})
    test_client.get(f"/book/{VALID_COMPETITION_NAME}/{VALID_CLUB_NAME}")
    response = test_client.post(
        "/purchase-places",
        data={
            "competition": VALID_COMPETITION_NAME,
            "club": VALID_CLUB_NAME,
            "places": PURCHASE_PLACES,
        },
    )
    assert response.status_code == 200
    result = int(VALID_CLUB_POINTS) - PURCHASE_PLACES
    assert f"Points available: {result}" in str(
        response.data
    )  # assert f"Points available: 7" in str(response.data)
    response = test_client.get("/logout")
    assert response.status_code == 302
    # _external use the absolute url: http://localhost/ instead of /
    assert response.location == url_for("index", _external=True)
    # response.location holt the redirected url http://localhost/ (home page)
    response = test_client.get(response.location)
    assert b"Welcome to the GUDLFT Registration Portal!" in response.data


def test_login_choose_invalid_competition(
    test_client,
    mock_clubs_valid,
    mock_clubs_invalid,
    mock_competitions_valid,
    mock_competitions_invalid,
):
    """
    GIVEN a Flask app for testing
    WHEN the urls: '/show-summary', '/book/<competition>/<club>' pages are requested (GET and POST)
        but the requested competition's date is in the past
    THEN checks if the competition date is in the past,
            invalid competition, stays on same page and displays error message:
                Sorry, but this competition is already over!
    """

    test_client.get("/")
    test_client.post("/show-summary", data={"email": VALID_CLUB_EMAIL})
    today = datetime.now().replace(microsecond=0)
    if INVALID_COMPETITION_DATE < str(today):
        response = test_client.get(
            f"/book/{INVALID_COMPETITION_NAME}/{INVALID_CLUB_NAME}"
        )
        assert response.status_code == 200
        assert b"Sorry, but this competition is already over!" in response.data
        assert f"Points available: {INVALID_CLUB_POINTS}" in str(response.data)
