from flask import render_template
from plantflask import app, db

@app.route("/")
def home():
    return "Home"

@app.route("/login")
def login():
    return render_template("login.html", title="Title")

# A web page interface to add plant weights
@app.route("/addweight")
def addweight():
    return "Add weight user interface"

# Displays the status of all plants
@app.route("/status")
def status():
    return "Plant statuses or stati"

# Plant event API url
@app.route("/pei", methods=['GET'])
def interface():
    return "Failed to add data to database"
