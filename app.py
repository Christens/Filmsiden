from flask import Flask, render_template

app = Flask(__name__)

from jsonapp import json_filmer

@app.route("/")
def index():
    return render_template("index.html", filmer=json_filmer())