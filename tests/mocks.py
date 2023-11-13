VALID_CLUB_EMAIL = "john@simplylift.co"
INVALID_CLUB_EMAIL = "john@simply.co"
VALID_CLUB_NAME = "Simply Lift"
INVALID_CLUB_NAME = "Invalid Club Name"
VALID_CLUB_POINTS = "13"
INVALID_CLUB_POINTS = "0"

VALID_COMPETITION_NAME = "Spring Festival"
INVALID_COMPETITION_NAME = "Invalid Competition Name"
VALID_COMPETITION_AVAILABLE_PLACES = "25"
VALID_COMPETITION_DATE = "2024-03-27 10:00:00"


def mock_load_clubs_valid():
    return [
        {
            "name": VALID_CLUB_NAME,
            "email": VALID_CLUB_EMAIL,
            "points": VALID_CLUB_POINTS,
        }
    ]


def mock_load_clubs_email_invalid():
    return [
        {
            "name": INVALID_CLUB_NAME,
            "email": INVALID_CLUB_EMAIL,
            "points": INVALID_CLUB_POINTS,
        }
    ]


def mock_load_competition_valid():
    return [
        {
            "name": VALID_COMPETITION_NAME,
            "date": VALID_COMPETITION_DATE,
            "number_of_places": VALID_COMPETITION_AVAILABLE_PLACES,
        }
    ]


def mock_load_competition_invalid_name():
    return [
        {
            "name": INVALID_COMPETITION_NAME,
            "date": "2024-03-27 10:00:00",
            "number_of_places": "25",
        }
    ]
