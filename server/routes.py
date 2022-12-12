from server import app, bcrypt, db
import urllib.request
from flask import jsonify, request, session
import random
import requests
from server.models import Events, User, Todos



def get_time():

    url = "http://worldtimeapi.org/api/timezone/Europe/Warsaw"
    response = requests.get(url)
    data = response.json()
    return data["week_number"]


@app.route("/", methods=['GET'])
def home():

    week_nr = int(get_time())
    url1 = "https://www.timeapi.io/api/Time/current/zone?timeZone=Europe/Warsaw"
    url2 = "http://worldtimeapi.org/api/timezone/Europe/Warsaw"
    response1 = requests.get(url1)
    response2 = requests.get(url2)
    data1 = response1.json()
    data2 = response2.json()

    week_number = str(data2["week_number"])
    month_number = str(data1["month"])
    day_month_number = str(data1["day"])
    day_week_number = str(data2["day_of_week"])
    year = str(data1["year"])

    return jsonify({
        "week_number": week_number,
        "month_number": month_number,
        "day_month_number": day_month_number,
        "day_week_number": day_week_number,
        "year": year
    })



@app.route('/test/<name>', methods =['POST'])
def test(name):
    xd = 'hi my name is: ' + name

    return jsonify({"text":xd})


@app.route('/event',methods=['POST'])
def event():
    user_id = 1
    starth = request.json['starth']
    startm = request.json['startm']
    duration = request.json['duration']
    week = request.json['week']
    desc = request.json['desc']
    title = request.json['title']
    day_of_week = request.json['day_of_week']
    year = request.json['year']
    day_of_month = request.json['day_of_month']
    month = request.json['month']

    new_event = Events(user_id = user_id, starth = starth, startm = startm,
                        duration = duration, week = week, desc = desc,
                        title = title, day_of_week = day_of_week, year = year,
                        day_of_month = day_of_month, month = month)

    db.session.add(new_event)
    db.session.commit()

    return "event has been added"

@app.route('/todo', methods=['POST'])
def todo():
    user_id = 1
    status = request.json['status']
    text = request.json['text']
    week = request.json['week']
    day_of_week = request.json['day_of_week']
    year = request.json['year']
    day_of_month = request.json['day_of_month']
    month = request.json['month']
    
    new_todos = Todos(user_id = user_id, status = status, text = text, week = week,
                      day_of_week = day_of_week, year = year, 
                      day_of_month = day_of_month, month = month)
    
    db.session.add(new_todos)
    db.session.commit()
    
    return "todos has ben added"
    
    
    
@app.route('/get_todos/<user>/<week>', methods=['GET'])
def get_todos(user, week):
    #do dokonczenia funkcjonalnosc
    return "XDD" + user +" XFDF"+week
    


@app.route('/user', methods=['POST'])
def add_user():
    email = request.json['email']
    new_user = User(email = email)
    db.session.add(new_user)
    db.session.commit()
    return "user has been added"


    


