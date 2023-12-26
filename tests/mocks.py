from datetime import datetime, timedelta

next_week_date = datetime.now() + timedelta(days=7)
last_week_date = datetime.now() - timedelta(days=7)

VALID_CLUB_EMAIL = "valid@email.com"
INVALID_CLUB_EMAIL = "invalid@email.com"
VALID_CLUB_NAME = "Valid Club Name"
INVALID_CLUB_NAME = "Invalid Club Name"
VALID_CLUB_POINTS = "13"
INVALID_CLUB_POINTS = "0"

VALID_COMPETITION_NAME = "Valid Competition Name"
INVALID_COMPETITION_NAME = "Invalid Competition Name"
VALID_COMPETITION_AVAILABLE_PLACES = "25"
VALID_COMPETITION_DATE = next_week_date.isoformat()
INVALID_COMPETITION_DATE = last_week_date.isoformat()


def mock_load_clubs_valid():
    """creates a mock for the function in server.py named: load_clubs"""

    return [
        {
            "name": VALID_CLUB_NAME,
            "email": VALID_CLUB_EMAIL,
            "points": VALID_CLUB_POINTS,
        }
    ]


def mock_load_clubs_invalid():
    """creates a mock for the function in server.py named: load_clubs with invalid data"""

    return [
        {
            "name": INVALID_CLUB_NAME,
            "email": INVALID_CLUB_EMAIL,
            "points": INVALID_CLUB_POINTS,
        }
    ]


def mock_load_competition_valid():
    """creates a mock for the function in server.py named: load_competitions"""

    return [
        {
            "name": VALID_COMPETITION_NAME,
            "date": VALID_COMPETITION_DATE,
            "number_of_places": VALID_COMPETITION_AVAILABLE_PLACES,
        }
    ]


def mock_load_competition_invalid():
    """creates a mock for the function in server.py named: load_competitions with invalid data"""

    return [
        {
            "name": INVALID_COMPETITION_NAME,
            "date": INVALID_COMPETITION_DATE,
            "number_of_places": "25",
        }
    ]
