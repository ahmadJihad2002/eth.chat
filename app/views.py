from flask import render_template
from app import app


@app.route('/')
def createAccout():
    return render_template("homePage.html")
