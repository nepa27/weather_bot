from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from keybords.for_questions import get_cities_kb
from utils.get_weather import get_weather

router = Router()

@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(
        'В каком городе вы хотите узнать погоду?\n'
        'Для перезапуска бота нажмите /stop, затем /start',
        reply_markup=get_cities_kb()
    )
@router.message(Command('stop'))
async def stop_conversation(message: Message):
    await message.answer('Бот остановлен. Нажмите /start, чтобы продолжить')

@router.message(F.location)
async def handle_location(message: Message):
    latitude = message.location.latitude
    longitude = message.location.longitude
    await message.answer(
        await get_weather(latitude, longitude)
    )

@router.message(F.text.lower() == 'курск' or
                F.text.lower() == 'москва' or
                F.text.lower() == 'череповец' or
                F.text.lower() == 'харовск' or
                F.text.lower() == 'колпашево')
async def answer_city(message: Message):
    await message.answer(
        await get_weather(message.text),
    )

@router.message(F.text.lower() == 'другой город')
async def ask_for_city_name(message: Message):
    await message.answer('Введите название города')

@router.message()
async def handle_custom_city(message: Message):
    await message.answer(
        await get_weather(message.text),
    )
