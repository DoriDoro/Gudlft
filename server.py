import json

from datetime import datetime
from flask import Flask, render_template, request, redirect, flash, url_for


app = Flask(__name__)
app.secret_key = "something_special"


def load_clubs():
    with open("clubs.json") as c:
        list_of_clubs = json.load(c)["clubs"]
        return list_of_clubs


def load_competitions():
    with open("competitions.json") as comps:
        list_of_competitions = json.load(comps)["competitions"]
        return list_of_competitions


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

    if matching_clubs:
        club = matching_clubs[0]
        return render_template("welcome.html", club=club, competitions=competitions)
    else:
        flash("Sorry, that email was not found.")
        return render_template("index.html")


@app.route("/book/<competition>/<club>")
def book(competition, club):
    """renders the chosen competition to book a place"""

    today = datetime.now().replace(microsecond=0)
    found_club = [c for c in clubs if c["name"] == club][0]
    found_competition = [c for c in competitions if c["name"] == competition][0]

    if found_club and found_competition["date"] > str(today):
        return render_template(
            "booking.html", club=found_club, competition=found_competition
        )
    else:
        flash("Sorry, but this competition is already over!")
        # return redirect(url_for("purchase_places"))
        return render_template("welcome.html", club=club, competitions=competitions)
        # http://127.0.0.1:5000/book/Fall Classic/Simply Lift

    # else:
    #      flash("Something went wrong-please try again")
    #      return render_template("welcome.html", club=club, competitions=competitions)


@app.route("/purchase-places", methods=["POST"])
def purchase_places():
    """
    checks if the secretary is trying to book:
        - more than 12 places at once
        - more places than available
        - more places than she can book
    """

    competition = [c for c in competitions if c["name"] == request.form["competition"]][
        0
    ]
    club = [c for c in clubs if c["name"] == request.form["club"]][0]
    places_required = int(request.form["places"])

    if (places_required <= int(club["points"])) and (places_required <= 12):
        competition["number_of_places"] = (
            int(competition["number_of_places"]) - places_required
        )
        club["points"] = int(club["points"]) - places_required
        flash("Great-booking complete!")
        return render_template("welcome.html", club=club, competitions=competitions)
    elif places_required > 12:
        flash("You can not book more than 12 places!")
        return render_template("booking.html", club=club, competition=competition)
    else:
        flash(f"You try to book more places than you have available!")
        return render_template("booking.html", club=club, competition=competition)


@app.route("/dashboard")
def dashboard():
    """display the points of the clubs"""

    return render_template("dashboard.html", clubs=clubs)


@app.route("/logout")
def logout():
    """logs user out"""

    return redirect(url_for("index"))
