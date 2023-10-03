"""
This file test_book.py contains the functional tests for the route book
- tests the listing of the competition, if valid (in future)
- tests the error message if a competition date is in the past
"""
from datetime import datetime


def test_book_valid_competition(test_app, clubs_fixture, competitions_fixture):
    """
    GIVEN a Flask app for testing
    WHEN the '/book' page is requested (GET)
    THEN checks if the competition date is in the future,
            valid competition, lists the competition to book a place
    """
    with test_app.test_client() as test_client:
        today = datetime.now().replace(microsecond=0)
        valid_competition = competitions_fixture[0]
        competition_name = valid_competition["name"]
        club_name = clubs_fixture[0]["name"]
        if valid_competition["date"] > str(today):
            response = test_client.get(f"/book/{competition_name}/{club_name}")
            assert response.status_code == 200
            assert b"Spring Festival" in response.data
            assert b"Places available:" in response.data


def test_book_invalid_competition(test_app, clubs_fixture, competitions_fixture):
    """
    GIVEN a Flask app for testing
    WHEN the '/book' page is requested (GET)
    THEN checks if the competition date is in the past,
            invalid competition, stays on same page
    """
    with test_app.test_client() as test_client:
        today = datetime.now().replace(microsecond=0)
        valid_competition = competitions_fixture[0]
        competition_name = valid_competition["name"]
        club_name = clubs_fixture[0]["name"]
        if valid_competition["date"] < str(today):
            response = test_client.get(f"/book/{competition_name}/{club_name}")
            assert response.status_code == 200
            assert b"Sorry, but this competition is already over!" in response.data
