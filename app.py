from flask import Flask, render_template, request

app = Flask(__name__)

from jsonapp import json_filmer
filmer = json_filmer()

from api import søk_etter_filmer
liste = []

@app.route("/")
def rute_index():
    return render_template("index.html", filmer=filmer)

@app.route("/sok", methods=["GET", "POST"])
def rute_sok():
    if request.method == "POST":
        svar = request.form["sok"]
        filmer = søk_etter_filmer(svar)
        liste.clear()
        for film in filmer:
            liste.append(film)
    return render_template("sok.html", søkeliste = liste)

@app.route("/populaert")
def rute_populaer():
    return render_template("populaert.html")