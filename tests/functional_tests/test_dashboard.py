"""
This file test_dashboard.py contains the functional tests for the route dashboard
- tests the listing of the club points
"""
from tests.mocks import VALID_CLUB_NAME


def test_dashboard(test_client, mock_clubs_valid):
    """
    GIVEN a Flask app for testing
    WHEN the '/dashboard' page is requested (GET)
    THEN checks if a table is listed with points of each club
    """

    response = test_client.get("/dashboard")
    assert response.status_code == 200
    assert VALID_CLUB_NAME in str(response.data)
    assert VALID_CLUB_NAME in str(response.data)
