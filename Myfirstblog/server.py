from Flask import Flask,render_template,url_for,redirect,request
import csv
from urllib import request,response

app=Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt',mode='a') as database:
        email = data['email']
        Subject = data['Subject']
        message = data['message']
        file = database.write(f'\n{email},{Subject},{message}')

def write_to_csv(data):
    with open('database.csv',newline='',mode='a') as database2:
        email = data['email']
        Subject = data['Subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,Subject,message])

@app.route('/submit_form',methods = ['POST','GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        #print(data)
        write_to_csv(data)
        return redirect('/database.html')
    else:
        return 'something went wrong !!'


app.run(debug=True)