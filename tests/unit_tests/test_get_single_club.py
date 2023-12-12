"""
This file test_get_single_club.py contains the unit tests for the function get_single_club in
server.py file.
- tests the function get_single_club:
    - successful outcome
    - failed outcome, None
"""

import server
from tests.mocks import mock_load_clubs_valid


def test_get_single_club_success(mock_clubs_valid):
    """
    GIVEN a Flask app for testing
    WHEN the function get_single_club is called
    THEN checks if the found club is a valid club
    """

    club_name = mock_load_clubs_valid()[0]["name"]
    assert server.get_single_club(club_name) == mock_load_clubs_valid()[0]


def test_get_single_club_fail(mock_clubs_valid):
    """
    GIVEN a Flask app for testing
    WHEN the function get_single_club is called
    THEN checks if the found club is None
    """

    club_name = "wrong_club_name"
    none_value = None
    assert server.get_single_club(club_name) == none_value
