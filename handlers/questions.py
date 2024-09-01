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

@router.message(F.text.lower() == 'курск')
async def answer_kursk(message: Message):
    await message.answer(
        get_weather(message.text),
    )

@router.message(F.text.lower() == 'москва')
async def answer_moscow(message: Message):
    await message.answer(
        get_weather(message.text),
    )

@router.message(F.text.lower() == 'череповец')
async def answer_cherepovetc(message: Message):
    await message.answer(
        get_weather(message.text),
    )

@router.message(F.text.lower() == 'харовск')
async def answer_cherepovetc(message: Message):
    await message.answer(
        get_weather(message.text),
    )

@router.message(F.text.lower() == 'колпашево')
async def answer_cherepovetc(message: Message):
    await message.answer(
        get_weather(message.text),
    )