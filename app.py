from  flask import Flask
from flask import render_template
from flask import request
import os


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    print(email, password)
    return "OK"

if __name__ == "__main__":
    app.run()
