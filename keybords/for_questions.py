from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_cities_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text='Текущая геопозиция', request_location=True)
    kb.button(text='Москва')
    kb.button(text='Курск')
    kb.button(text='Череповец')
    kb.button(text='Колпашево')
    kb.button(text='Харовск')
    kb.button(text='Другой город')
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)