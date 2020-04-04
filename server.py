from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

""" @app.route('/')
def hello_world():
    return 'Hello, Gene!' """

@app.route('/')
def home_page():
    return render_template('index.html')

# streamline page addressing and rendering use variable in url string to hold page name

@app.route('/<string:page_name>')
def html_render_page(page_name):
    return render_template(page_name)

# added submit form route 
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    #return 'form submitted!'
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return redirect('/thankyou.html')
    else:
         return 'something went wrong, Try Again'

#removed below rev 1.0 4/4/20
""" @app.route('/about.html')
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
    return render_template('services.html') """



