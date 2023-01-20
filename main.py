import flask
import requests
import os

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/Interests")
def Interests():
    return flask.render_template("I.html")

@app.route("/User")
def User():
    return flask.render_template("page2.html")

@app.route("/Team")
def Team():
    return flask.render_template("page3.html")

@app.route("/IP")
def IP():
    return flask.render_template("page4.html")
@app.route("/EP")
def EP():
    return flask.render_template("page5.html")

@app.route("/proc")
def processing():
    return flask.render_template("page1.html")
    
@app.route("/music")
def music():
    return flask.render_template("music.html")

@app.route("/electronics")
def electronics():
    return flask.render_template("electronics.html")

@app.route("/other")
def other():
    return flask.render_template("otherWork.html")

@app.route("/ex")
def ex():
    return flask.render_template("ex.html")

app.run(debug=False, host = '0.0.0.0')