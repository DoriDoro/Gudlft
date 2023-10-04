"""
This file test_logout.py contains the functional tests for the route logout
"""


def test_logout(test_app):
    """
    GIVEN a Flask app for testing
    WHEN the '/logout' page is requested (GET)
    THEN check if response is valid and redirect to '/'
    """

    with test_app.test_client() as test_client:
        response = test_client.get("/logout")
        assert response.status_code == 302
        assert b"Welcome to the GUDLFT Registration Portal!"
