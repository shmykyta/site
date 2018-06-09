from app import app
from flask import render_template
import os

@app.route('/')
def StartWithHello():
    return '<h1>Hello, World!!!!!</h1>'

@app.route('/user/')
def say_hello():
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

@app.route('/user/')
def read_file():
    from settings import APP_STATIC
    open_file = open(os.path.join(APP_STATIC, 'some_file.txt'))
    read_value = open_file.read()
    open_file.close()
    return  render_template('index.html',
                            read_value = read_value)



