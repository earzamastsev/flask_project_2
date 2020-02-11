from  flask import Flask
from flask import render_template
from flask import request
from data import *

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/goals/<goal>/')
def goal(goal):
    return render_template('goal.html', goal=goal)

@app.route('/profiles/<teacher_id>/')
def profile(teacher_id):
    return render_template('profile.html', teacher_id=teacher_id)

@app.route('/request/')
def request():
    return render_template('request.html')

@app.route('/request_done/', methods=['POST'])
def request_done():
    return render_template('request_done.html')

@app.route('/booking/<teacher_id>/<day>/<time>/')
def booking(teacher_id, day, time):
    return render_template('booking.html', teacher_id=teacher_id, day=day, time=time)

@app.route('/booking_done/', methods=['POST'])
def booking_done():
    return render_template('booking_done.html')

if __name__ == "__main__":
    app.run()
