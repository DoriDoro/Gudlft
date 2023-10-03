"""
This file test_index.py contains the functional tests for the route index
"""
from server import app


def test_index():
    """
    GIVEN a Flask app for testing
    WHEN the '/' page is requested (GET)
    THEN check if response is valid
    """

    test_app = app
    test_app.config["TESTING"] = True  # set the app to testing mode

    with test_app.test_client() as test_client:
        response = test_client.get("/")
        assert response.status_code == 200
        assert b"Welcome to the GUDLFT Registration Portal!" in response.data
        assert b"Please enter your secretary email to continue:" in response.data
