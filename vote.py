import logging
import requests
import json

from flask import Flask
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app,"/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG);

@ask.launch
def launch():
    welcome = 'Welcome to find my rep. Let me know where you from?'
    return question(welcome)

@ask.intent('CityFindIntent', mapping={'city': 'City'} )
def get_rep(city):
    info = getReps(city)
    return statement(info)

@ask.intent('AMAZON.StopIntent')
def stop():
    return statement("Goodbye")


@ask.intent('AMAZON.CancelIntent')
def cancel():
    return statement("Goodbye")

@ask.session_ended
def session_ended():
    return "", 200

def getReps(city):
    key = 'AIzaSyDCSzaHH_Hu_VHUHrgGNqgmXu9rUzLlVro';
    base = 'https://www.googleapis.com/civicinfo/v2/representatives';
    url = base + '?address=' + city + '&key=' + key;

    response = requests.get(url)

    entire_response  = response.json()

    officials = []

    for names in entire_response['officials']:
        officials.append(names['name'].encode('ascii'))

    senators = officials[2:4]
    senator_names = " and ".join(senators)

    return senator_names

if __name__ == '__main__':
    app.run(debug=True)
