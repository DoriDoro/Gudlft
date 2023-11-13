"""
This file test_dashboard_login_book_logout.py contains an integration test. It will test to go to
dashboard, login of one secretary, purchase of places of a valid competition and logout.
- tests the login with pytest-mock
- tests the purchase of places of one competition
"""
from tests.mocks import (
    mock_load_clubs_valid,
    mock_load_competition_valid,
    VALID_CLUB_NAME,
    VALID_CLUB_EMAIL,
    VALID_CLUB_POINTS,
    VALID_COMPETITION_NAME,
    VALID_COMPETITION_AVAILABLE_PLACES,
)

PLACES_INPUT_VALID = 5


def test_dashboard_login_book_logout(mocker, test_client):
    mocker.patch("server.load_clubs", mock_load_clubs_valid)
    mocker.patch("server.load_competitions", mock_load_competition_valid)

    response = test_client.get("/dashboard")
    assert response.status_code == 200
    assert VALID_CLUB_NAME in str(response.data)

    response = test_client.post("/show-summary", data={"email": VALID_CLUB_EMAIL})
    assert response.status_code == 200
    assert f"Welcome, {VALID_CLUB_EMAIL}" in str(response.data)
    # assert f"Points available: {VALID_CLUB_POINTS}" in str(response.data)

    response = test_client.get(f"/book/{VALID_COMPETITION_NAME}/{VALID_CLUB_NAME}")
    assert response.status_code == 200
    assert VALID_COMPETITION_NAME in str(response.data)
    # assert f"Places available: {VALID_COMPETITION_AVAILABLE_PLACES}" in str(
    #     response.data
    # )

    response = test_client.post(
        "/purchase-places",
        data={
            "competition": VALID_COMPETITION_NAME,
            "club": VALID_CLUB_NAME,
            "places": PLACES_INPUT_VALID,
        },
    )
    assert response.status_code == 200
    assert b"Great-booking complete!"

    response = test_client.get("/logout")
    assert response.status_code == 302
    assert b"Welcome to the GUDLFT Registration Portal!"
