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
    while len(nummerliste) < 3:
        tall = randint(0, 249)
        if tall not in nummerliste:
            nummerliste.append(tall)
    return nummerliste

def tilfeldig_2nr():
    nummerliste = []
    while len(nummerliste) < 2:
        tall = randint(0, 249)
        if tall not in nummerliste:
            nummerliste.append(tall)
    return nummerliste

favoritter = []
for film in filmer:
    ny_favoritt = Favoritt(film["navn"])
    favoritter.append(ny_favoritt)

def øk_favorittpoeng(filmnavn):
    for film in favoritter:
        if film._navn == filmnavn:
            film.øk_poeng()

indexFavorittpoeng = []
def index_Favorittpoeng(nummerliste, favoritter=favoritter):
    for nummer in nummerliste:
        for film in favoritter:
            if favoritter.index(film) == nummer:
                indexFavorittpoeng.append(film.hent_poeng())

indexFavoritter = []
def oppdater_favorittliste():
    for film in favoritter:
        if film.hent_poeng() > 0:
            ny_liste = []
            ny_liste.append(film.hent_navn())
            ny_liste.append(film.hent_poeng())
            indexFavoritter.append(ny_liste)

def sorter():
    global indexFavoritter
    indexFavoritterS = []
    minst = 1
    størst = 0
    for film in indexFavoritter:
        if film[1] > størst:
            størst = film[1]
    for i in range(minst,størst+1):
        for film in indexFavoritter:
            if film[1] == i:
                indexFavoritterS.insert(0,film)
    return indexFavoritterS

@app.route("/")
def rute_index():
    tilfeldig = tilfeldig_2nr()
    indexFavorittpoeng.clear()
    index_Favorittpoeng(tilfeldig)
    indexFavoritter.clear()
    oppdater_favorittliste()
    favoritterS = sorter()
    return render_template("index.html", filmer=filmer, tilfeldige_nummer=tilfeldig, indexFavorittpoeng=indexFavorittpoeng, favoritter=favoritterS)

@app.route("/sok", methods=["GET", "POST"])
def rute_sok():
    try:
        if request.method == "POST":
            svar = request.form["sok"]
            filmer = søk_etter_filmer(svar)
            søkeliste.clear()
            for film in filmer:
                søkeliste.append(film)
        return render_template("sok.html", søkeliste=søkeliste)
    except:
        return render_template("error.html")

@app.route("/anbefalt")
def rute_anbefalt():
    anbefalt_nummer = tilfeldig_3nr()
    return render_template("anbefalt.html", filmer=filmer, anbefalt_nummer=anbefalt_nummer)

@app.route("/øk-favorittpoeng/<filmnavn>", methods=["POST"])
def rute_øk_faovrittpoeng(filmnavn):
    øk_favorittpoeng(filmnavn)
    return rute_index()

app.run(debug=True)