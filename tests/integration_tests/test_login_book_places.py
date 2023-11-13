"""
This file test_login_book_places.py contains an integration test. It will test the login of one
secretary and one purchase of places of a competition.
- tests the login with pytest-mock
- tests the purchase of places of one competition
"""
from tests.mocks import (
    mock_load_clubs_valid,
    mock_load_competition_valid,
    VALID_CLUB_EMAIL,
    VALID_CLUB_NAME,
    VALID_CLUB_POINTS,
    VALID_COMPETITION_NAME,
)

PLACES_INPUT = 5


def test_login_and_book_places(mocker, test_client):
    mocker.patch("server.load_clubs", mock_load_clubs_valid)
    mocker.patch("server.load_competitions", mock_load_competition_valid)

    response = test_client.post("/show-summary", data={"email": VALID_CLUB_EMAIL})
    assert response.status_code == 200
    assert f"Welcome, {VALID_CLUB_EMAIL}" in str(response.data)
    assert f"Points available: {VALID_CLUB_POINTS}" in str(response.data)

    response = test_client.get(f"/book/{VALID_COMPETITION_NAME}/{VALID_CLUB_NAME}")
    assert response.status_code == 200
    assert VALID_COMPETITION_NAME in str(response.data)
    assert f"Places available:" in str(response.data)

    response = test_client.post(
        "/purchase-places",
        data={
            "competition": VALID_COMPETITION_NAME,
            "club": VALID_CLUB_NAME,
            "places": PLACES_INPUT,
        },
    )
    assert response.status_code == 200
    assert b"Great-booking complete!"
