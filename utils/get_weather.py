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
     'Mist': '\U0001F32B'
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
                weather = weather_json['weather'][0]['description']
                weather_description = weather_json['weather'][0]['main']
                icon = ''
                if weather_description in CODE_TO_SMAIL:
                    icon = CODE_TO_SMAIL[weather_description]

                geo = 'текущей геопозиции' if city == '' else f'городе {city}'
                return (f'Температура в {geo} - {temperature} '
                        f'градусов\n'
                        f'В {geo} сейчас {weather} {icon}')
            except KeyError:
                return 'Нет данных'