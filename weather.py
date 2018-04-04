# coding=utf-8

import settings
import requests
import json
import settings

from datetime import datetime, time
import utils

class Day(object):

    def __init__(self, data, is_current_date, *args, **kwargs):
        self.date = datetime.combine(datetime.fromtimestamp(data["time"]), time.min)
        self.is_current_date = is_current_date
        self.summary = data.get('summary', '')
        self.icon = utils.icon_lookup.get(data.get('icon'))
        self.wind_speed = data.get('windSpeed')
        self.temperature = data.get("apparentTemperature") or \
            utils.average_daily_temperature(data["apparentTemperatureLow"],data["apparentTemperatureHigh"])

    def __unicode__(self):
        return u"[{}] Vent : {}, Température : {}, Icon : {}, aujourd'hui ? : {}"\
            .format(self.date, self.wind_speed, self.temperature, self.icon,self.is_current_date)

class Weather(object):
    # region Ctor
    def __init__(self, *args, **kwargs):
        self.base_url = settings.WEARTHER_API_URL
        self.lat = settings.WEATHER_LAT
        self.lon = settings.WEATHER_LON
    # endregion

    # region Methods
    def get_data(self):
        r = requests.get(self.base_url)
        print r, self.base_url
        data = json.loads(r.text)
        self.days = [Day(x if not utils.is_current_date(x['time']) else data["currently"],
                         utils.is_current_date(x['time'])) for x in data["daily"]["data"]]
        return self
    # endregion
