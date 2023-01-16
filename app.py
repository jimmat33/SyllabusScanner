'''
This is the main file for runnning and routing

To activate environment:
conda activate FlaskProj

To run: 
flask --app app run

To debug:
flask --app app --debug run

'''

from flask import Flask, render_template, url_for
from models import Schema

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/login')
def login():
    return 'This is the login page'


if __name__ == "__main__":
    Schema()
    app.run(debug=True)
