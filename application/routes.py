
from application import app
from flask import render_template

@app.route('/')
def base():
    return render_template("signup.html")

@app.route('/login')
def login():
    return render_template("login.html")
