from aiogram.types import ReplyKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton


buttons = [[
    KeyboardButton(text="Довідка")

]]

start_menu = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, one_time_keyboard=True)
