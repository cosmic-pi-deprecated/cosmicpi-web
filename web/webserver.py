# from XRootD import client
from flask import Flask, render_template, url_for, send_from_directory
from datetime import datetime
# import pygal
# from pygal.style import LightSolarizedStyle
# from detector import Event
import random

from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient()
db = client.cosmicpi_db
events = db.events


@app.route("/")
def home():
    now = datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")

    data = list()
    # with open('test/test.txt', 'r') as f:
    #     bits = f.readline().split()
    #     previous = datetime.fromtimestamp(int(bits[0]) / 1e9)
    #     energy = ((int(bits[2]) + int(bits[4])) / 2) * 0.2
    #     data.append([0, energy])
    #
    #     for line in f:
    #         bits = line.split()
    #
    #         current = datetime.fromtimestamp(int(bits[0]) / 1e9)
    #         delta = current - previous
    #         delay = (delta.seconds * 1000.0) + (delta.microseconds / 1000.0)
    #         previous = current
    #
    #         energy = ((int(bits[2]) + int(bits[4])) / 2) * 0.2
    #         data.append([delay, energy])
    #
    #     # Make a copy and shuffle it
    #     data2 = data[:]
    #     random.shuffle(data2)

    templateData = {
        'title': 'Muon detector web interface',
        'time': timeString,
        # 'events': events,
        # 'chart': chart,
        'node_id': 10,
        'data': data,
        # 'data2': data2,
        'events': events.find()
    }

    return render_template('main.html', **templateData)


@app.route("/ol3")
def ol3_test():
    templateData = {
        'title': 'ol3 test'
    }

    return render_template('map.html', **templateData)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
