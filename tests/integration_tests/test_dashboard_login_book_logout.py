"""
This file test_dashboard_login_book_logout.py contains an integration test. It will test to go to
dashboard, login of one secretary, purchase of places of a valid competition and logout.
- tests the login with pytest-mock
- tests the purchase of places of one competition
"""
from tests.mocks import (
    mock_load_clubs_valid,
    mock_load_competition_valid,
)
from tests.functional_tests.test_book import test_book_valid_competition
from tests.functional_tests.test_dashboard import test_dashboard
from tests.functional_tests.test_logout import test_logout
from tests.functional_tests.test_purchase_places import test_purchase_places_successful
from tests.functional_tests.test_show_summary import test_show_summary_successful_login

PLACES_INPUT_VALID = 5


def test_dashboard_login_book_logout(mocker, test_client):
    mocker.patch("server.load_clubs", mock_load_clubs_valid)
    mocker.patch("server.load_competitions", mock_load_competition_valid)

    test_dashboard(test_client)
    test_show_summary_successful_login(test_client)
    test_book_valid_competition(test_client)
    test_purchase_places_successful(test_client)
    test_logout(test_client)

    # test_client.post("/show-summary", data={"email": VALID_CLUB_EMAIL})
    #
    # test_client.get(f"/book/{VALID_COMPETITION_NAME}/{VALID_CLUB_NAME}")
    #
    # response = test_client.post(
    #     "/purchase-places",
    #     data={
    #         "competition": VALID_COMPETITION_NAME,
    #         "club": VALID_CLUB_NAME,
    #         "places": 5,
    #     },
    #
    #     competition["number_of_places"] = 15
    # )
    # assert response.status_code == 200
    # assert b"Great-booking complete!"
    # competition["number_of_places"] = 10
    # # if the amount has changed   competition["number_of_places"] has changed
