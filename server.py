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

    email = request.form["email"]
    club = next((club for club in clubs if club["email"] == email), None)

    if club is None:
        flash("Sorry, that email was not found.")
        return render_template("index.html")

    return render_template("welcome.html", club=club, competitions=competitions)


"""matching_clubs = [club for club in clubs if club["email"] == request.form["email"]]

    if not matching_clubs:
        flash("Sorry, that email was not found.")
        return render_template("index.html")
    club = matching_clubs[0]
    return render_template("welcome.html", club=club, competitions=competitions)"""


"""
improvements:
    - use only dictionary instead of list and dictionary
    - use a generator expression instead of a list comprehension to create 'club'.
      The next function is used to get the first item from the generator, or 'None' if the 
      generator is empty.
    
def show_summary():
   email = request.form["email"]
   club = next((club for club in clubs if club["email"] == email), None)

   if club is None:
       flash("Sorry, that email was not found.")
       return render_template("index.html")

   return render_template("welcome.html", club=club, competitions=competitions)
"""


@app.route("/book/<competition>/<club>")
def book(competition, club):
    """renders the chosen and valid competition to book a place
    if invalid competition error"""

    today = datetime.now().replace(microsecond=0)

    found_club = next((c for c in clubs if c["name"] == club), None)
    if found_club is None:
        flash("Sorry, but this club is not found!")

    found_competition = next(
        (c for c in competitions if c["name"] == competition), None
    )
    if found_competition is None:
        flash("Sorry, but this competition is not found!")

    if found_competition["date"] < str(today):
        flash("Sorry, but this competition is already over!")
        return render_template(
            "welcome.html", club=found_club, competitions=competitions
        )
    return render_template(
        "booking.html", club=found_club, competition=found_competition
    )


"""    today = datetime.now().replace(microsecond=0)
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
    )"""


"""
improvements:
    - use only dictionary instead of list and dictionary
    - use a generator expression instead of a list comprehension to create 'club'.
      The next function is used to get the first item from the generator, or 'None' if the 
      generator is empty.
    - check if club and competition are existing before accessing them
    
def book(competition, club):

   today = datetime.now().replace(microsecond=0)

   found_club = next((c for c in clubs if c["name"] == club), None)
   if found_club is None:
       flash("Sorry, but this club is not found!")
       
   found_competition = next((c for c in competitions if c["name"] == competition), None)
   if found_competition is None:
       flash("Sorry, but this competition is not found!")

   if found_competition["date"] < str(today):
       flash("Sorry, but this competition is already over!")
       return render_template(
           "welcome.html", club=found_club, competitions=competitions
       )
   return render_template(
       "booking.html", club=found_club, competition=found_competition
   )
"""


@app.route("/purchase-places", methods=["POST"])
def purchase_places():
    """
    books places for a competition and
    checks if the secretary is trying to book:
        - more than 12 places at once
        - more places than available
        - more places than she can book
    """

    competition_name = request.form["competition"]
    club_name = request.form["club"]
    places_required = int(request.form["places"])

    competition = next((c for c in competitions if c["name"] == competition_name), None)
    if competition is None:
        flash("Competition not found!")
    club = next((c for c in clubs if c["name"] == club_name), None)
    if club is None:
        flash("Club not found.")

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


"""competition = [c for c in competitions if c["name"] == request.form["competition"]]
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
    return render_template("welcome.html", club=club, competitions=competitions)"""


"""
improvements:
    - use only dictionary instead of list and dictionary
    - use a generator expression instead of a list comprehension to create 'club'.
      The next function is used to get the first item from the generator, or 'None' if the 
      generator is empty.
    - check if club and competition are existing before accessing them
    
def purchase_places():

   competition_name = request.form["competition"]
   club_name = request.form["club"]
   places_required = int(request.form["places"])

   competition = next((c for c in competitions if c["name"] == competition_name), None)
   if competition is None:
       flash("Competition not found!")
   club = next((c for c in clubs if c["name"] == club_name), None)
   if club is None:
       flash("Club not found.")

   if places_required > int(club["points"]):
       flash("You try to book more places than you have points available!")
   if places_required > int(competition["number_of_places"]):
       flash("You try to book more than there are places available!")
   if places_required > 12:
       flash("You can not book more than 12 places!")
   if places_required == 0:
       flash("Please chose a number between 1 and 12!")

   competition["number_of_places"] = (
       int(competition["number_of_places"]) - places_required
   )
   club["points"] = int(club["points"]) - places_required
   flash("Great-booking complete!")
   return render_template("welcome.html", club=club, competitions=competitions)
"""


"""
improvement: use Exceptions instead of flash messages
    - have to create a new template 404.html

from flask import abort

class ClubNotFound(Exception):
  pass

class CompetitionNotFound(Exception):
  pass

@app.route("/purchase-places", methods=["POST"])
def purchase_places():

   competition_name = request.form["competition"]
   club_name = request.form["club"]
   places_required = int(request.form["places"])

   competition = next((c for c in competitions if c["name"] == competition_name), None)
   if competition is None:
       abort(404, description="Competition not found.")
   club = next((c for c in clubs if c["name"] == club_name), None)
   if club is None:
       abort(404, description="Club not found.")

   if places_required > int(club["points"]):
       abort(400, description="You try to book more places than you have points available!")
   if places_required > int(competition["number_of_places"]):
       abort(400, description="You try to book more than there are places available!")
   if places_required > 12:
       abort(400, description="You can not book more than 12 places!")
   if places_required == 0:
       abort(400, description="Please chose a number between 1 and 12!")

   competition["number_of_places"] = (
       int(competition["number_of_places"]) - places_required
   )
   club["points"] = int(club["points"]) - places_required
   flash("Great-booking complete!")
   return render_template("welcome.html", club=club, competitions=competitions)

@app.errorhandler(404)
def handle_404(e):
  return render_template('404.html'), 404

@app.errorhandler(400)
def handle_400(e):
  return render_template('400.html', error_message=e.description), 400
"""


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
