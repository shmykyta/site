from app import app

@app.route('/')
def StartWithHello():
    return '<h1>Hello, World!!!!!</h1>'

@app.route('/user/<username>')
def SayHelloToSomeone(username):
    return '<h1>Hello, %s !</h1>' % username
