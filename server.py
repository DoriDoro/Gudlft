import json

from datetime import datetime
from flask import Flask, render_template, request, redirect, flash, url_for


def load_clubs():
    with open("clubs.json") as c:
        list_of_clubs = json.load(c)["clubs"]
        return list_of_clubs


def load_competitions():
    with open("competitions.json") as comps:
        list_of_competitions = json.load(comps)["competitions"]
        return list_of_competitions


app = Flask(__name__)
app.secret_key = "something_special"

competitions = load_competitions()
clubs = load_clubs()


@app.route("/")
def index():
    """renders the index.html home page"""

    return render_template("index.html")


@app.route("/show-summary", methods=["POST"])
def show_summary():
    """checks if the email address is correct, if email is false, error message
    displays a list of competitions"""

    matching_clubs = [club for club in clubs if club["email"] == request.form["email"]]

    if not matching_clubs:
        flash("Sorry, that email was not found.")
        return render_template("index.html")
    club = matching_clubs[0]
    return render_template("welcome.html", club=club, competitions=competitions)


@app.route("/book/<competition>/<club>")
def book(competition, club):
    """renders the chosen and valid competition to book a place
    if invalid competition error"""

    today = datetime.now().replace(microsecond=0)
    # if found_club is empty, it will be None instead of an error:
    found_club = [c for c in clubs if c["name"] == club]
    found_club = found_club.pop() if found_club else None
    found_competition = [c for c in competitions if c["name"] == competition]
    found_competition = found_competition.pop() if found_competition else None

    if found_club and found_competition["date"] < str(today):
        flash("Sorry, but this competition is already over!")
        return render_template(
            "welcome.html", club=found_club, competitions=competitions
        )
    return render_template(
        "booking.html", club=found_club, competition=found_competition
    )


@app.route("/purchase-places", methods=["POST"])
def purchase_places():
    """
    books places for a competition and
    checks if the secretary is trying to book:
        - more than 12 places at once
        - more places than available
        - more places than she can book
    """

    competition = [c for c in competitions if c["name"] == request.form["competition"]]
    competition = competition.pop() if competition else None
    club = [c for c in clubs if c["name"] == request.form["club"]]
    club = club.pop() if club else None
    places_required = int(request.form["places"])

    error_message = None

    if places_required > int(club["points"]):
        error_message = "You try to book more places than you have points available!"
    if places_required > int(competition["number_of_places"]):
        error_message = "You try to book more than there are places available!"
    if places_required > 12:
        error_message = "You can not book more than 12 places!"
    if places_required == 0:
        error_message = "Please chose a number between 1 and 12!"

    if error_message is not None:
        flash(error_message)
        return render_template("booking.html", club=club, competition=competition)

    competition["number_of_places"] = (
        int(competition["number_of_places"]) - places_required
    )
    club["points"] = int(club["points"]) - places_required
    flash("Great-booking complete!")
    return render_template("welcome.html", club=club, competitions=competitions)


@app.route("/dashboard")
def dashboard():
    """display the points of the clubs"""

    return render_template("dashboard.html", clubs=clubs)


@app.route("/logout")
def logout():
    """logs user out"""

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()
