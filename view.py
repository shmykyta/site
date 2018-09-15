from app import app
from flask import render_template, request, send_from_directory, url_for, jsonify
import os
from werkzeug import secure_filename
import hashlib



basedir = os.path.abspath(os.path.dirname(__file__))

@app.route('/')
def StartWithHello():
    return '<h1>This is root page, nothing to do here, go to <a href="/user">/user</a></h1>'

@app.route('/user/')
def say_hello():
    posts = [
        {
            'main': 'Task',
            'body': 'Show information about file include hashsum'
        },
        {
            'main': 'Result',
            'body': 'seems working'
        }
            ]

    return render_template("index.html",
        title = 'Upload files',
        posts = posts)

app.config['ALLOWED_EXTENSIONS'] = set(['doc', 'docx', 'txt', 'pdf', 'png', 'jpg'])
app.config['MAX_CONTENT_LENGTH'] =  1024 * 1024 * 10

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'js_static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     'static/js', filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    elif endpoint == 'css_static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     'static/css', filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


@app.route('/css/<path:filename>')
def css_static(filename):
    return send_from_directory(app.root_path + '/static/css/', filename)


@app.route('/js/<path:filename>')
def js_static(filename):
    return send_from_directory(app.root_path + '/static/js/', filename)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploadajax', methods=['POST', 'GET'])
def upldfile():
    if request.method == 'POST':
        files = request.files['file']
        if files and allowed_file(files.filename):
            filename = secure_filename(files.filename)
            app.logger.info('FileName: ' + filename)
            updir = os.path.join(basedir, 'upload/')
            files.save(os.path.join(updir, filename))
            file_size = os.path.getsize(os.path.join(updir, filename))
            hashsum = hashlib.md5(filename.encode('utf-8')).hexdigest()
            with open('upload/Link.txt', 'w') as file:
                file.write(hashsum)
            return jsonify(name=filename, size=file_size, hashsum=hashsum)

