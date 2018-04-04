# coding=utf-8

from flask import Flask, render_template, send_from_directory
from weather import Weather
import settings

app = Flask(__name__, static_url_path='/static')

@app.route('/<path:path>')
def serve_static(path):
	return send_from_directory('static', path)

def get_weather():
    weather = Weather().get_data()
    return weather

@app.route('/')
def home():
    context = {
        "weather": get_weather()
    }

    return render_template('index.html', context=context)
