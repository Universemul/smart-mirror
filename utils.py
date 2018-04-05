# coding=utf-8
from datetime import datetime, time

icon_lookup = {
    'clear-day': "img/Sun.png",  # clear sky day
    'wind': "img/Wind.png",   #wind
    'cloudy': "img/Cloud.png",  # cloudy day
    'partly-cloudy-day': "img/PartlySunny.png",  # partly cloudy day
    'rain': "img/Rain.png",  # rain day
    'snow': "img/Snow.png",  # snow day
    'snow-thin': "img/Snow.png",  # sleet day
    'fog': "img/Haze.png",  # fog day
    'clear-night': "img/Moon.png",  # clear sky night
    'partly-cloudy-night': "img/PartlyMoon.png",  # scattered clouds night
    'thunderstorm': "img/Storm.png",  # thunderstorm
    'tornado': "img/Tornado.png",    # tornado
    'hail': "img/Hail.png"  # hail
}

PERIODIC_RSS_TASK = 15 # in seconds


def is_current_date(ts, now=datetime.now()):
    date = datetime.combine(datetime.fromtimestamp(ts), time.min)
    return datetime.combine(datetime.now(), time.min) == date

def average_daily_temperature(low, high):
    return (low + high) / 2
