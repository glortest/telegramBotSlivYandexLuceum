
""""5381154310:AAHGvmHoo6StoC8_UpcIjZ8bWt4rVAccdzs"""
from data_base import *
import logging
from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler

import datetime


async def start(update, context):
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет {user.mention_html()}! Я эхо-бот. Напишите мне что-нибудь, и я пришлю это назад!",
    )


async def help_command(update, context):
    await update.message.reply_text("Я пока не умею помогать... Я только ваше эхо.")



# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def echo(update, context):
    print(update.message.text)
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

    text_handler = MessageHandler(filters.TEXT, echo)

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
        return "Ой-ой, похоже, решение этой задачи доступно только с премиум аккаунтом"
    else:
        return "похоже, вы ошиблись и не правильно ввели текст"


if __name__ == '__main__':
    main()