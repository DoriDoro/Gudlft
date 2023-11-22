"""
This file test_dashboard_login_book_logout.py contains an integration test. It will test to go to
dashboard, login of one secretary, purchase of places of a valid competition and logout.
- tests the login with pytest-mock
- tests the purchase of places of one competition
"""
from flask import url_for

from tests.mocks import (
    mock_load_clubs_valid,
    mock_load_competition_valid,
    VALID_CLUB_EMAIL,
    VALID_COMPETITION_NAME,
    VALID_CLUB_NAME,
    VALID_CLUB_POINTS,
)

PURCHASE_PLACES = 6


def test_dashboard_login_book_logout(mocker, test_client):
    """
    GIVEN a Flask app for testing
    WHEN the urls: '/dashboard', '/', '/show-summary', '/book/<competition>/<club>',
        '/purchase-places' and '/logout' page is requested (GET and POST)
    THEN check if available points are correct in response and
        if the redirect to the home page is working
            use:
            - valid club
            - valid competition
            - 6 places
    """

    mocker.patch("server.load_clubs", mock_load_clubs_valid)
    mocker.patch("server.load_competitions", mock_load_competition_valid)

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
