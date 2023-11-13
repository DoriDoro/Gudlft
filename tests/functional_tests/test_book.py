"""
This file test_book.py contains the functional tests for the route book
- tests the listing of the competition, if valid (in future)
- tests the error message if a competition date is in the past
"""
from datetime import datetime

from tests.mocks import (
    VALID_CLUB_NAME,
    INVALID_CLUB_NAME,
    VALID_COMPETITION_NAME,
    INVALID_COMPETITION_NAME,
    VALID_COMPETITION_DATE,
)


def test_book_valid_competition(test_client):
    """
    GIVEN a Flask app for testing
    WHEN the '/book' page is requested (GET)
    THEN checks if the competition date is in the future,
            valid competition, lists the competition to book a place
    """

    today = datetime.now().replace(microsecond=0)
    if VALID_COMPETITION_DATE > str(today):
        response = test_client.get(f"/book/{VALID_COMPETITION_NAME}/{VALID_CLUB_NAME}")
        assert response.status_code == 200
        assert VALID_COMPETITION_NAME in str(response.data)
        assert b"Places available:" in response.data


def test_book_invalid_competition(test_client):
    """
    GIVEN a Flask app for testing
    WHEN the '/book' page is requested (GET)
    THEN checks if the competition date is in the past,
            invalid competition, stays on same page
    """

    today = datetime.now().replace(microsecond=0)
    if VALID_COMPETITION_DATE < str(today):
        response = test_client.get(
            f"/book/{INVALID_COMPETITION_NAME}/{INVALID_CLUB_NAME}"
        )
        assert response.status_code == 200
        assert b"Sorry, but this competition is already over!" in response.data
