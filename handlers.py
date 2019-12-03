from bs4 import BeautifulSoup
from utility import get_keyboard
import requests

def sms(bot,update):
    print('Кто-то отправил команду /start. Что мне делать?')
    bot.message.reply_text('Привет, коллега {}! \nПолучи случайное пожедание от своих коллег.'
                           ' \nНапиши пожелание для своих коллег'.format(bot.message.chat.first_name), reply_markup=get_keyboard())

def get_cogratulation(bot,update):
    pass

def write_congratulation(bot,update):
    pass

# функция parrot() отвечает темже сообщением которое ему прислали
def parrot(bot, update):
    print(bot.message.text)  # печатаем на экран сообщение пользователя
    bot.message.reply_text(bot.message.text)  # отправляем обратно текс который пользователь послал
