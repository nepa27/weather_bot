import os

from dotenv import load_dotenv
from aiohttp import ClientSession


load_dotenv('.env')
APP_ID = os.environ.get('APP_ID')

CODE_TO_SMAIL = {
     'Clear': '\U00002600',
     'Clouds': '\U00002601',
     'Rain': '\U00002614',
     'Drizzle': '\U00002614',
     'Thunderstorm': '\U000026A1',
     'Snow': '\U0001F328',
     'Mist': '\U0001F32B',
     'Wind': '\U0001F32C',
     'House': '\U0001F3E0',
     'Thermometer': '\U0001F321'
}

async def get_weather(*args):
    async with ClientSession() as session:
        if len(args) == 1:
            city = args[0]
            params = {
                'q':city,
                'units':'metric',
                'lang':'ru',
                'appid':APP_ID
            }
            url = 'https://api.openweathermap.org/data/2.5/weather'
        else:
            city = ''
            latitude, longitude = args
            params = {
                'lat':latitude,
                'lon':longitude,
                'units':'metric',
                'lang':'ru',
                'appid':APP_ID
            }
            url = 'https://api.openweathermap.org/data/2.5/weather?'
        async with session.get(url=url, params=params) as response:
            weather_json = await response.json()
            try:
                temperature = round(weather_json['main']['temp'])
                temperature_feels_like = round(weather_json['main']['feels_like'])
                speed_wind = round(weather_json['wind']['speed'])
                weather = weather_json['weather'][0]['description']
                weather_description = weather_json['weather'][0]['main']
                icon = ''

                if weather_description in CODE_TO_SMAIL:
                    icon = CODE_TO_SMAIL[weather_description]
                wind_icon = CODE_TO_SMAIL['Wind']
                house_icon = CODE_TO_SMAIL['House']
                term_icon = CODE_TO_SMAIL['Thermometer']
                geo = 'текущей геопозиции' if city == '' else f'городе {city} {house_icon}'
                return (f'Температура {term_icon} в {geo}: {temperature} градусов\n'
                        f'Ощущается как {temperature_feels_like} градусов\n'
                        f'В {geo} сейчас {weather} {icon}\n'
                        f'Скорость ветра: {speed_wind} м/с {wind_icon}')
            except KeyError:
                return 'Нет данных'