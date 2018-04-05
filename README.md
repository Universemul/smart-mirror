Smart Mirror which can display news, weather, calendar events

## Status 

[![Build Status](https://travis-ci.org/Universemul/smart-mirror.svg?branch=master)](https://travis-ci.org/Universemul/smart-mirror)

## Installation and Updating
Clone the repository.

```
git git@github.com:Universemul/smart-mirror.git
```

## Install your dependencies 
make sure you have `pip` installed before doing this

```
(sudo) pip install -r requirements.txt
```

## Add your api token

```
vim settings.py
```

Replace `WEATHER_API_KEY` with the token you got from https://darksky.net

You can also customize some variables :

`WEATHER_API_KEY`

`WEATHER_LANG`

`WEATHER_LAT` and `WEATHER_LON`

`WEATHER_UNITS`

Please check https://darksky.net/dev/docs for more informations

## Running
To run the application run the following command in this folder

```
export FLASK_APP=main.py
python -m flask run
```

Open your browser and enter `http://127.0.0.1:5000/` on your address bar
