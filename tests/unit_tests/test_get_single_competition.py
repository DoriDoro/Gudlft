"""
This file test_get_single_competition.py contains the unit tests for the function get_single_competiotion in
server.py file.
- tests the function get_single_competition:
    - successful outcome
    - failed outcome, None
"""

import server
from tests.mocks import mock_load_competition_valid


def test_get_single_club_success(mock_competitions_valid):
    """
    GIVEN a Flask app for testing
    WHEN the function get_single_competition is called
    THEN checks if the found club is a valid club
    """

    competition_name = mock_load_competition_valid()[0]["name"]
    assert (
        server.get_single_competition(competition_name)
        == mock_load_competition_valid()[0]
    )


def test_get_single_club_fail(mock_competitions_valid):
    """
    GIVEN a Flask app for testing
    WHEN the function get_single_competition is called
    THEN checks if the found club is None
    """

    competition_name = "wrong_club_name"
    none_value = None
    assert server.get_single_competition(competition_name) == none_value
