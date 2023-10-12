"""
This file test_index.py contains the functional tests for the route index
"""


def test_index(test_client):
    """
    GIVEN a Flask app for testing
    WHEN the '/' page is requested (GET)
    THEN check if response is valid
    """

    response = test_client.get("/")
    assert response.status_code == 200
    assert b"Welcome to the GUDLFT Registration Portal!" in response.data
    assert b"Please enter your secretary email to continue:" in response.data
