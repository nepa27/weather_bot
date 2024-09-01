import os

from dotenv import load_dotenv
import requests


load_dotenv('.env')
WEATHER_TOKEN = os.environ.get('WEATHER_TOKEN')

def get_weather(city):
    try:
        # https://wttr.in/
        url = (f'https://api.openweathermap.org/data/2.5/weather?'
               f'q={city}&units=metric&lang=ru&'
               f'appid=79d1ca96933b0328e1c7e3e7a26cb347')

        request = requests.get(url).json()
        temperature = round(request['main']['temp'])
        temperature_feels = round(request['main']['feels_like'])
    except BaseException as er:
        print(er)
    return (f'Температура в городе {city} - {temperature} градусов\n'
            f'Ощущается как {temperature_feels} градусов')

