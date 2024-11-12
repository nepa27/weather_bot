# Телеграмм-бот для получения данных о погоде
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
## Описание
Бот, который отправляет данные о погоде по запросу.
## Основные особенности
- Возможность получения данных о погоде в конкретном городе;
- Возможность получения данных о погоде по геопозиции.
## Стек использованных технологий
+ Python 3.11
+ aiogram
+ asynco

## Запуск проекта
1. Клонируйте репозиторий на ваш локальном компьютере:

```
git clone https://github.com/nepa27/weather_bot
cd weather_bot
```
   
2. Установите и активируйте виртуальное окружение c учетом версии Python 3.11:
* Если у вас Linux/macOS

```
 python3 -m venv env
 source env/bin/activate
```

* Если у вас Windows

```
 python -m venv venv
 source venv/Scripts/activate
```

+ Обновите менеджер пакетов pip:

```
python -m pip install --upgrade pip
```

+ Затем установите зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

+ Запускаем скрипт командой:

```
python main.py
```

2. Для правильной работы бота создайте TELEGRAM_TOKEN и APP_ID в файле .env:

 ```
 TELEGRAM_TOKEN       # токен телеграмм-бота
 APP_ID               # идентификатор для работы с api.openweathermap.org
 ```
   
## Автор

+ [Александр Непочатых](https://github.com/nepa27) 
