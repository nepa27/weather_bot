from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_cities_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text='Москва')
    kb.button(text='Курск')
    kb.button(text='Череповец')
    return kb.as_markup(resize_keyboard=True)