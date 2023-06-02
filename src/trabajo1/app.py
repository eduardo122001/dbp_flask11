import random
from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

""""
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
"""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/more")
def more():
    return render_template("more.html")

@app.route("/loop")
def loop():
    names = ["Alice", "Bob", "Charlie"]
    return render_template("loop.html", names=names)

@app.route("/variable0")
def variable0():
    headline = "Hello, world!"
    return render_template("variable0.html", headline=headline)

@app.route("/aleatorio")
def aleatorio():
    headline = random.choice(["Hello, world!", "Hi there!", "Good morning!"])
    return render_template("aleatorio.html", headline=headline)
"""
notes = []

@app.route("/static", methods=["GET", "POST"])
def static():
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)

    return render_template("static.html", notes=notes)
"""