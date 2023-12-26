"""
This file test_purchase_places.py contains the functional tests for the route purchase_places
    tests the process of booking places
    tests if a secretary:
        - books more than 12 places at once
        - books more places than club points available
"""

from Python_Testing.tests.mocks import (
    VALID_CLUB_NAME,
    VALID_COMPETITION_NAME,
    VALID_COMPETITION_AVAILABLE_PLACES,
)


def test_purchase_places_failed_booking_more_than_12_places(
    test_client, mock_clubs_valid, mock_competitions_valid
):
    """
    GIVEN a Flask app for testing
    WHEN the '/purchase_places' page is requested (POST) with more than 12 places
    THEN check if response is valid and the secretary has NOT booked places
        use:
        - valid club
        - valid competition
        - 15 places
        for testing
    """

    response = test_client.post(
        "/purchase-places",
        data={
            "club": VALID_CLUB_NAME,
            "competition": VALID_COMPETITION_NAME,
            "places": 77,
        },
    )
    assert response.status_code == 200
    assert b"You can not book more than 12 places!" in response.data
    assert f"Places available: {VALID_COMPETITION_AVAILABLE_PLACES}" in str(
        response.data
    )


def test_purchase_places_successful(
    test_client, mock_clubs_valid, mock_competitions_valid
):
    """
    GIVEN a Flask app for testing
    WHEN the '/purchase_places' page is requested (POST)
    THEN check if response is valid and the secretary has booked places
        use:
        - valid club
        - valid competition
        - 6 places
        for testing
    """

    response = test_client.post(
        "/purchase-places",
        data={
            "competition": VALID_COMPETITION_NAME,
            "club": VALID_CLUB_NAME,
            "places": 6,
        },
    )
    assert response.status_code == 200
    assert b"Great-booking complete!" in response.data
    assert f"Points available: 7" in str(response.data)


def test_purchase_places_failed_booking_zero_places(
    test_client, mock_clubs_valid, mock_competitions_valid
):
    """
    GIVEN a Flask app for testing
    WHEN the '/purchase_places' page is requested (POST) with more than club points available
    THEN check if response is valid and the secretary has NOT booked places
        use:
        - valid club
        - valid competition
        - 0 places
        for testing
    """

    response = test_client.post(
        "/purchase-places",
        data={
            "club": VALID_CLUB_NAME,
            "competition": VALID_COMPETITION_NAME,
            "places": 0,
        },
    )
    assert response.status_code == 200
    assert b"Please chose a number between 1 and 12!" in response.data
