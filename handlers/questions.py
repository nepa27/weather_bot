from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from keybords.for_questions import get_cities_kb

router = Router()

@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(
        'В каком городе вы хотите узнать погоду?',
        reply_markup=get_cities_kb()
    )

@router.message(F.text.lower() == 'курск')
async def answer_kursk(message: Message):
    await message.answer(
        'Курск',
    )

@router.message(F.text.lower() == 'москва')
async def answer_moscow(message: Message):
    await message.answer(
        'Москва',
    )

@router.message(F.text.lower() == 'череповец')
async def answer_cherepovetc(message: Message):
    await message.answer(
        'Череповец',
    )