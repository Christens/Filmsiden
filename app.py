from flask import Flask, render_template

app = Flask(__name__)

from jsonapp import json_filmer
filmer = json_filmer()

@app.route("/")
def rute_index():
    return render_template("index.html", filmer=filmer)

@app.route("/sok")
def rute_sok():
    return render_template("sok.html")

@app.route("/populaert")
def rute_populaer():
    return render_template("populaert.html")