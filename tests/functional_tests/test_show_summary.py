"""
This file test_show_summary.py contains the functional tests for the route show_summary
- tests the login with email,
- tests the failed login with email
- tests the display of the competitions on the website with url show-summary/
"""
from tests.mocks import VALID_CLUB_EMAIL, INVALID_CLUB_EMAIL


def test_show_summary_successful_login(test_client, mock_clubs_valid):
    """
    GIVEN a Flask app for testing
    WHEN the '/show-summary' page is requested (POST)
    THEN check if response is valid
        use the first club email for testing
    """

    response = test_client.post("/show-summary", data={"email": VALID_CLUB_EMAIL})
    assert response.status_code == 200
    assert f"Welcome, {VALID_CLUB_EMAIL}" in str(response.data)


def test_show_summary_failed_login(test_client, mock_clubs_valid):
    """
    GIVEN a Flask app for testing
    WHEN the '/show-summary' page is requested (POST)
    THEN check if response is valid but with wrong email address
        use wrong email for testing
    """

    response = test_client.post("/show-summary", data={"email": INVALID_CLUB_EMAIL})
    assert response.status_code == 200
    assert b"Sorry, that email was not found." in response.data
