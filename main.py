# coding=utf-8

import utils
import settings
import functools
import threading
import time

from flask import Flask, render_template, send_from_directory, jsonify
from flask_socketio import SocketIO, emit, send

from weather import Weather
from rss import RssFluxUpdater

# http://numberoverzero.com/posts/2017/07/17/periodic-execution-with-asyncio
app = Flask(__name__, static_url_path='/static')
rss_updater = RssFluxUpdater(limit=3)
# region Misc

def get_weather():
    weather = Weather().get_data()
    return weather

@app.route('/rss')
def periodic_rss():
    data = rss_updater.fetch()
    return jsonify(data)

# endregion

# region Url
@app.route('/')
def home():
    context = {
        "weather": get_weather(),
    }
    return render_template('index.html', context=context)

@app.route('/<path:path>')
def serve_static(path):
	return send_from_directory('static', path)
# endregion
