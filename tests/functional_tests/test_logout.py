"""
This file test_logout.py contains the functional tests for the route logout
"""
from flask import url_for


def test_logout(test_client):
    """
    GIVEN a Flask app for testing
    WHEN the '/logout' page is requested (GET)
    THEN check if response is valid and redirect to '/'
    """

    response = test_client.get("/logout")
    assert response.status_code == 302
    # _external use the absolute url: http://localhost/ instead of /
    assert response.location == url_for("index", _external=True)
    # response.location holt the redirected url http://localhost/ (home page)
    response = test_client.get(response.location)
    assert b"Welcome to the GUDLFT Registration Portal!" in response.data
