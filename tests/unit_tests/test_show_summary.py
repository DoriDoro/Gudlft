"""
This file test_show_summary.py contains the functional tests for the route show_summary
- tests the login with email,
- tests the failed login with email
- tests the display of the competitions on the website with url show-summary/
"""


def test_show_summary_successful_login(test_client, clubs_fixture):
    """
    GIVEN a Flask app for testing
    WHEN the '/show-summary' page is requested (POST)
    THEN check if response is valid
        use the first club email for testing
    """

    club_email = clubs_fixture[0]["email"]
    response = test_client.post("/show-summary", data={"email": club_email})
    assert response.status_code == 200
    assert b"Welcome, john@simplylift.co" in response.data


def test_show_summary_failed_login(test_client):
    """
    GIVEN a Flask app for testing
    WHEN the '/show-summary' page is requested (POST)
    THEN check if response is valid but with wrong email address
        use wrong email for testing
    """

    response = test_client.post("/show-summary", data={"email": "john@simplylift.c"})
    assert response.status_code == 200
    assert b"Welcome to the GUDLFT Registration Portal!" in response.data
