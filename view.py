from app import app
from flask import render_template, request
import os
from werkzeug import secure_filename

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
  #  from settings import APP_STATIC
   # open_file = open(os.path.join(APP_STATIC, 'some_file.txt'))
   # data = open_file.read()
    #print(open_file())
    with open(os.path.join('/Users/nikita/PycharmProjects/app/assert', 'some_file.txt')) as value:
        read_value = value.read()
    return  render_template('index.html', read_value = read_value)


@app.route('/user/')
def upload_file():
    return render_template('upload.html')


@app.route('/user/', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'

