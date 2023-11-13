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
    INVALID_CLUB_NAME,
    VALID_CLUB_POINTS,
    VALID_COMPETITION_NAME,
    INVALID_COMPETITION_NAME,
    VALID_COMPETITION_AVAILABLE_PLACES,
)

PLACES_INPUT_VALID = 5
PLACES_INPUT_INVALID = 13


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
    assert f"Places available: {VALID_COMPETITION_AVAILABLE_PLACES}" in str(
        response.data
    )

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


def test_login_and_book_invalid_competition(mocker, test_client):
    mocker.patch("server.load_clubs", mock_load_clubs_valid)
    mocker.patch("server.load_competitions", mock_load_competition_valid)

    response = test_client.post("/show-summary", data={"email": VALID_CLUB_EMAIL})
    assert response.status_code == 200
    assert f"Welcome, {VALID_CLUB_EMAIL}" in str(response.data)
    # assert f"Points available: {VALID_CLUB_POINTS}" in str(response.data)

    response = test_client.get(f"/book/{INVALID_COMPETITION_NAME}/{INVALID_CLUB_NAME}")
    assert response.status_code == 200
    assert b"Sorry, but this competition is already over!" in response.data


def test_login_purchase_invalid_places_input(mocker, test_client):
    mocker.patch("server.load_clubs", mock_load_clubs_valid)
    mocker.patch("server.load_competitions", mock_load_competition_valid)

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
            "places": PLACES_INPUT_INVALID,
        },
    )
    assert response.status_code == 200
    assert b"You can not book more than 12 places!"
