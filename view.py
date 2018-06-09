from app import app
from flask import render_template

@app.route('/')
def StartWithHello():
    return '<h1>Hello, World!!!!!</h1>'

@app.route('/user/')
def SayHello():
    user = { 'nickname': 'Shubas' }
    posts = [
        {
            'author': {'nickname': 'Shubas'},
            'body': 'This is my start in web-dev'
        },
        {
            'author': {'nickname': 'Mokich'},
            'body': 'I have more commits than Shubas'
        }
            ]
    return render_template("index.html",
        title = 'This is',
        user = user,
        posts = posts)


