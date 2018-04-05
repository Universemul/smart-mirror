# coding=utf-8

WEATHER_API_KEY = "494c92a3a55543f5f38764cb56c374f0" #Dark Sky API
WEATHER_LANG = "fr"
WEATHER_LAT = 50.6292
WEATHER_LON = 3.0573
WEATHER_UNITS = 'si'
WEARTHER_API_URL = "https://api.darksky.net/forecast/{api_key}/{lat},{lon}?lang={lang}&exclude=minutely,hourly&units={units}"\
    .format(api_key=WEATHER_API_KEY, lang=WEATHER_LANG, lat=WEATHER_LAT, lon=WEATHER_LON, units=WEATHER_UNITS)

LOCALE = "fr"

APP_NAME = "Smart Mirror"

RSS_FLUX = "https://www.numerama.com/feed/"

