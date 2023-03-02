from flask import Flask, render_template, request
from random import randint
from favoritt import Favoritt

app = Flask(__name__)

from jsonapp import json_filmer
filmer = json_filmer()

from api import søk_etter_filmer
søkeliste = []

def tilfeldig_3nr():
    nummerliste = []
    for i in range(3):
        nummerliste.append(randint(0,249))
    return nummerliste

def tilfeldig_2nr():
    nummerliste = []
    for i in range(2):
        nummerliste.append(randint(0,249))
    return nummerliste

favoritter = []
for film in filmer:
    ny_favoritt = Favoritt(film["navn"])
    favoritter.append(ny_favoritt)

def øk_favorittpoeng(filmnavn):
    for film in favoritter:
        if film.self._navn == filmnavn:
            film.øk_poeng()

indexFavorittpoeng = []
def index_Favorittpoeng(nummerliste, favoritter=favoritter):
    for nummer in nummerliste:
        for film in favoritter:
            if favoritter.index(film) == nummer:
                indexFavorittpoeng.append(film.hent_poeng())

@app.route("/")
def rute_index():
    tilfeldig = tilfeldig_2nr()
    indexFavorittpoeng.clear()
    index_Favorittpoeng(tilfeldig)
    print(indexFavorittpoeng)
    return render_template("index.html", filmer=filmer, tilfeldige_nummer=tilfeldig, indexFavorittpoeng=indexFavorittpoeng)

@app.route("/sok", methods=["GET", "POST"])
def rute_sok():
    if request.method == "POST":
        svar = request.form["sok"]
        filmer = søk_etter_filmer(svar)
        søkeliste.clear()
        for film in filmer:
            søkeliste.append(film)
    return render_template("sok.html", søkeliste=søkeliste)

@app.route("/anbefalt")
def rute_anbefalt():
    anbefalt_nummer = tilfeldig_3nr()
    return render_template("anbefalt.html", filmer=filmer, anbefalt_nummer=anbefalt_nummer)

@app.route("/øk-favorittpoeng/<filmnavn>", methods=["POST"])
def rute_øk_faovrittpoeng(filmnavn):
    øk_favorittpoeng(filmnavn)
    print(filmnavn)
    return rute_index()