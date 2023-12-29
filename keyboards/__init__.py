from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

from templates import *


def get_empty_keyboard():
    return ReplyKeyboardRemove(remove_keyboard=True)


def get_back_keyboard():
    buttons = [
        [KeyboardButton(text=BUTTON_BACK)]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)


def get_menu_keyboard():
    buttons = [
        [KeyboardButton(text=BUTTON_STATUS), KeyboardButton(text=BUTTON_MODEL)],
        [KeyboardButton(text=BUTTON_AUTH)]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)


def get_model_keyboard():
    buttons = [
        [KeyboardButton(text=BUTTON_LIGHTING)],
        [KeyboardButton(text=BUTTON_TEMPERATURE)],
        [KeyboardButton(text=BUTTON_HUMIDITY)],
        [KeyboardButton(text=BUTTON_BACK)]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
