from server import app, bcrypt, db
import urllib.request
from flask import jsonify, request, session
import random
import requests
from server.models import Events, User, Todos


@app.route("/", methods=['GET'])
def home():

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
    todos_ = Todos.query.filter_by(user_id = user, week = week).all()
    todos = []
    
    for item in todos_:
        todo_ = Todos.query.filter_by(id = int(item.id)).first()
        todo = {
            "id":todo_.id,
            "status": todo_.status,
            "text": todo_.text,
            "week": todo_.week,
            "day_of_week": todo_.day_of_week,
            "day_of_month": todo_.day_of_month,
            "year": todo_.year,
            "month": todo_.month
        }
        todos.append(todo)
    return jsonify(todos) 


@app.route('/get_events/<user>/<week>', methods=['GET'])
def get_events(user, week):
    events_ = Events.query.filter_by(user_id = user, week = week).all()
    events = []
    
    for item in events_:
        event_ = Events.query.filter_by(id = int(item.id)).first()
        event = {
            "id":event_.id,
            "starth": event_.starth,
            "startm": event_.startm,
            "duration": event_.duration,
            "title":event_.title,
            "desc": event_.desc,
            "week": event_.week,
            "day_of_week": event_.day_of_week,
            "day_of_month": event_.day_of_month,
            "year": event_.year,
            "month": event_.month
        }
        events.append(event)
    return jsonify(events) 

@app.route('/user', methods=['POST'])
def add_user():
    email = request.json['email']
    new_user = User(email = email)
    db.session.add(new_user)
    db.session.commit()
    return "user has been added"


    


