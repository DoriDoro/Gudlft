"""
This file test_purchase_places.py contains the functional tests for the route purchase_places
    tests the process of booking places
    tests if a secretary:
        - books more than 12 places at once
        - books more places than club points available
"""


def test_purchase_places_successful(test_client, clubs_fixture, competitions_fixture):
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

    club = clubs_fixture[0]
    competition = competitions_fixture[0]
    nb_places = 3
    response = test_client.post(
        "/purchase-places",
        data={
            "club": club["name"],
            "competition": competition["name"],
            "places": nb_places,
        },
    )
    assert response.status_code == 200
    assert b"Great-booking complete!" in response.data


def test_purchase_places_failed_booking_more_than_12_places(
    test_client, clubs_fixture, competitions_fixture
):
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

    club = clubs_fixture[0]
    competition = competitions_fixture[0]
    nb_places = 13
    response = test_client.post(
        "/purchase-places",
        data={
            "club": club["name"],
            "competition": competition["name"],
            "places": nb_places,
        },
    )
    assert response.status_code == 200
    assert b"You can not book more than 12 places!" in response.data


def test_purchase_places_failed_booking_more_places_than_points(
    test_client, clubs_fixture, competitions_fixture
):
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

    club = clubs_fixture[1]
    competition = competitions_fixture[0]
    nb_places = 6
    response = test_client.post(
        "/purchase-places",
        data={
            "club": club["name"],
            "competition": competition["name"],
            "places": nb_places,
        },
    )
    assert response.status_code == 200
    assert b"You try to book more places than you have available!" in response.data
