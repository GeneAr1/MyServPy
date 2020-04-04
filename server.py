from flask import Flask, render_template
app = Flask(__name__)

""" @app.route('/')
def hello_world():
    return 'Hello, Gene!' """

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/project.html')
def projects(username=None):
    return render_template('project.html')

@app.route('/contact.html')
def contact(username=None):
    return render_template('contact.html')

@app.route('/services.html')
def services(username=None):
    return render_template('services.html')



