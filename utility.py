# Импортируем необходимые компоненты
from telegram import ReplyKeyboardMarkup
from telegram import KeyboardButton


SMILE = ['😊', '😀', '😇', '🤠', '😎', '🤓', '👶', '🧑‍🚀', '👮', '🦸', '🧟']
CALLBACK_BUTTON_GET_CONGRATULATION = "Прочитать пожелания 🏞"
CALLBACK_BUTTON_WRITE_CONGRATULATION = "Написать пожелание 🖌"
CALLBACK_BUTTON_START = "Начать 🎰"


# функция создает клавиатуру и ее разметку
def get_keyboard():
        my_keyboard = ReplyKeyboardMarkup([[CALLBACK_BUTTON_START],
                                         [CALLBACK_BUTTON_GET_CONGRATULATION, CALLBACK_BUTTON_WRITE_CONGRATULATION]
                                         ], resize_keyboard=True)  # добавляем кнопки
        return my_keyboard

