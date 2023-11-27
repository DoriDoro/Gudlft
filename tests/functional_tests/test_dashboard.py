"""
This file test_dashboard.py contains the functional tests for the route dashboard
- tests the listing of the club points
"""
import tests.mocks as mock


def test_dashboard(test_client, mocker):
    """
    GIVEN a Flask app for testing
    WHEN the '/dashboard' page is requested (GET)
    THEN checks if a table is listed with points of each club
    """

    mocker.patch("server.load_clubs", mock.mock_load_clubs_valid)

    response = test_client.get("/dashboard")
    assert response.status_code == 200
    assert mock.VALID_CLUB_NAME in str(response.data)
    assert mock.VALID_CLUB_NAME in str(response.data)
