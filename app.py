from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", activeHome="active")

@app.route("/metronome")
def metronome():
    return render_template("metronome.html", activeMetronome="active")

@app.route("/tap-tempo")
def tapTempo():
    return render_template("tap-tempo.html", activeTaptempo="active")

@app.route("/tuner")
def tuner():
    return render_template("tuner.html", activeTuner="active")