from flask import Flask, render_template, url_for, request, redirect
import csv

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

#write data to text file persists but hard to use
def write_to_datafile(data):
    with open('database.txt', mode='a') as database:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{name},{email},{subject},{message}')

# Write data to a CSV file easier to work with than the text files created a 
# csv_writer object to do the writing
def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,subject,message])


# added submit form route 
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    #return 'form submitted!'
    if request.method == 'POST':
        try:
           data = request.form.to_dict()
           #print(data)
           #write_to_datafile(data)
           write_to_csv(data)
           return redirect('/thankyou.html')
        except:
            return 'did not save to database'
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



