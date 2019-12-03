from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from settings import TG_TOKEN, TG_API_URL
from handlers import *



def main():
    my_bot = Updater(TG_TOKEN, TG_API_URL, use_context=True)
    my_bot.dispatcher.add_handler(CommandHandler('start', sms))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('Начать'), sms))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('Прочитать пожелания 🏞'), get_cogratulation))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('Написать пожелание 🖌'), write_congratulation))

    my_bot.start_polling()  # проверяет о наличии сообщений с платформы Telegram
    my_bot.idle()  # бот будет работать пока его не остановят


if __name__ == "__main__":
    main()
