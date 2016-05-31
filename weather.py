#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import json


def get_city_id(city_name):
    return 28698


def get_weather(city_name=u'Омск', day=0):
    url = "http://api.openweathermap.org/data/2.5/forecast/weather?q=Omsk&APPID=6b7f7032437d87b45a04ea317b721c9a&lang=ru&units=metric"
    s = urllib2.urlopen(url)
    answer = json.loads(s.read())
    day_weather = answer['list'][day]
    return {
        'temp': day_weather['main']['temp'],
        'description': day_weather['weather'][0]['description']
    }



if __name__ == '__main__':
    print get_weather()