"""
This file test_show_summary.py contains the functional tests for the route show_summary
- tests the login with email,
- tests the failed login with email
- tests the display of the competitions on the website with url show-summary/
"""


def test_show_summary_login(test_client, clubs_fixture):
    """
    GIVEN a Flask app for testing
    WHEN the '/show-summary' page is requested (POST)
    THEN check if response is valid
    """

    club_email = clubs_fixture[0]["email"]

    response = test_client.get("/show-summary")
    assert response.status_code == 200


# def test_show_summary_():

# def test_show_summary_():
