"""
This file test_purchase_places.py contains the functional tests for the route purchase_places
    tests the process of booking places
    tests if a secretary:
        - books more than 12 places at once
        - books more places than club points available
"""
from tests.mocks import VALID_CLUB_NAME, VALID_COMPETITION_NAME

PLACES_INPUT_VALID = 5
PLACES_INPUT_INVALID = 13
PLACES_INPUT_MORE_THAN_AVAILABLE = 6


def test_purchase_places_successful(test_client):
    """
    GIVEN a Flask app for testing
    WHEN the '/purchase_places' page is requested (POST)
    THEN check if response is valid and the secretary has booked places
        use:
        - the first club
        - the first competition
        - 3 places
        for testing
    """

    response = test_client.post(
        "/purchase-places",
        data={
            "competition": VALID_COMPETITION_NAME,
            "club": VALID_CLUB_NAME,
            "places": PLACES_INPUT_VALID,
        },
    )
    assert response.status_code == 200
    assert b"Great-booking complete!" in response.data


def test_purchase_places_failed_booking_more_than_12_places(test_client):
    """
    GIVEN a Flask app for testing
    WHEN the '/purchase_places' page is requested (POST) with more than 12 places
    THEN check if response is valid and the secretary has NOT booked places
        use:
        - the first club
        - the first competition
        - 13 places
        for testing
    """

    response = test_client.post(
        "/purchase-places",
        data={
            "club": VALID_CLUB_NAME,
            "competition": VALID_COMPETITION_NAME,
            "places": PLACES_INPUT_INVALID,
        },
    )
    assert response.status_code == 200
    assert b"You can not book more than 12 places!" in response.data


def test_purchase_places_failed_booking_more_places_than_points(test_client):
    """
    GIVEN a Flask app for testing
    WHEN the '/purchase_places' page is requested (POST) with more than club points available
    THEN check if response is valid and the secretary has NOT booked places
        use:
        - the second club
        - the first competition
        - 6 places
        for testing
    """

    response = test_client.post(
        "/purchase-places",
        data={
            "club": VALID_CLUB_NAME,
            "competition": VALID_COMPETITION_NAME,
            "places": PLACES_INPUT_MORE_THAN_AVAILABLE,
        },
    )
    assert response.status_code == 200
    assert b"You try to book more places than you have available!" in response.data
