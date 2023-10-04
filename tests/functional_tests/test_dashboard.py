"""
This file test_dashboard.py contains the functional tests for the route dashboard
- tests the listing of the club points
"""


def test_dashboard(test_app, clubs_fixture):
    """
    GIVEN a Flask app for testing
    WHEN the '/dashboard' page is requested (GET)
    THEN checks if a table is listed with points of each club
    """

    with test_app.test_client() as test_client:
        response = test_client.get("/dashboard")
        assert response.status_code == 200
        assert b"Simply Lift" in response.data
        assert b"Iron Temple" in response.data
        assert b"She Lifts" in response.data
