
from flask import Flask, render_template, url_for, redirect
from flask import request
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    #print(url_for('static', filename='static/favicon.ico'))
    return render_template('index.html')

# Dyanamically visible page

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

#database access
def write_to_file(data):
   with open('database.txt', mode='a') as database:
       email = data["email"]
       subject = data["subject"]
       message = data["message"]
       file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
   with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


# The Request Object
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        #print(data)
        return redirect('/thankyou.html')
        #return 'Form Submitted Successfully'
    else:
        return 'Something went wrong. please try again'

# statically visible page

#@app.route("/about.html")
#def about():
#    return render_template('about.html')

#@app.route("/works.html")7:
#def work():
#    return render_template('works.html')

#@app.route("/contact.html")
#def work():
#    return render_template('contact.html')

