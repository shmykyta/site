from app import app
from flask import render_template

@app.route('/')
def StartWithHello():
    return '<h1>Hello, World!!!!!</h1>'

@app.route('/user/')
def SayHello():
    user = { 'nickname': 'Shubas' }
    return render_template("index.html",
        title = 'This is',
        user = user)
