from flask import Flask, render_template
app = Flask(__name__)

""" @app.route('/')
def hello_world():
    return 'Hello, Gene!' """

@app.route('/home')
def home_page():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/<username>')
def hello_world(username=None):
    return render_template('user.html', name=username)



