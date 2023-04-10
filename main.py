from pickle import loads, dumps, load, dump
import json

""""5381154310:AAHGvmHoo6StoC8_UpcIjZ8bWt4rVAccdzs"""
import logging
from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler

import datetime



# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def preobrazovanieUvedomleniy(update, context):
    print('id: ' + str(update.message.from_user.id) + '; username: ' +
          str(update.message.from_user.username) + '; name: ' + str(update.message.from_user.first_name) + ' ' +
          str(update.message.from_user.last_name) + ' -> ' + str(update.message.text))
    print(str(update.message.from_user.id) +
               str(update.message.from_user.username) +
               str(update.message.from_user.first_name) +

               str(update.message.from_user.last_name))

    premium = (str(update.message.from_user.id) +
               str(update.message.from_user.username) +
               str(update.message.from_user.first_name) +
               str(update.message.from_user.last_name)
               )

    await update.message.reply_text(checkingAvailability(update.message.text, premium))


def main():
    application = Application.builder().token("5381154310:AAHGvmHoo6StoC8_UpcIjZ8bWt4rVAccdzs").build()

    text_handler = MessageHandler(filters.TEXT, preobrazovanieUvedomleniy)

    application.add_handler(text_handler)

    application.run_polling()


def proverka_na_premium(message):
    f = open("CashUsers.txt", "r", encoding="utf8")
    lines = [elem.strip() + "" for elem in f.readlines()]
    f.close()
    print(lines)
    print(message)
    for elem in lines:
        if elem == message:
            print(elem)

            return True
    return False


def checkingAvailability(text, premium):
    if text in free_db.keys():
        return free_db[text]
    elif text in cash_db.keys() and proverka_na_premium(premium):
        return cash_db[text]
    elif text in cash_db.keys():
        return "Ой-ой-ой, похоже, решение этой задачи доступно только с премиум аккаунтом"
    elif text == "/start":
        return """
Салам Алейкум. Это бот, который решает задачи яндекс лицея первого года обученя. Чтобы узнать как работает бот, пиши /help
Поскольку решение задач - являние времязатратное, в нашем боте доступны не все решения. Чтобы разблокировать полный доступ, пиши /vip"""

    elif text == "/help":
        return """ 
Чтобы узнать решение задачи необходимо просто написать её название в чат с этим ботом.
остались вопросы -> @glortest"""

    elif text == "/vip":
        return """
Друг, ты ступил на путь истины, на путь 80ти баллов за первый год обучения, написав эту команду. 
Для полной разблокировки бота необходимо - перевести N рублей на номер +N(NNN)NNN-NN-NN по СБП. 
После оплаты в чат бота напиши такое сообщение: /+N(), поместив внутрь скобок свой номер телефона. 
Потом придётся подожди нексколько минут, а затем наслаждаться жизнью, ведь не придётся ботать ЯЛ"""
    elif text[:4] == "/+N(":
        return "Теперь придётся немного подождать"

    else:
        return "похоже, вы ошиблись и не правильно ввели текст"


if __name__ == '__main__':
    with open('db_cash.json') as filej:
        cash_db = json.load(filej)
    with open('db_free.json') as filej:
        free_db = json.load(filej)
    main()
