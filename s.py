from telegram import ReplyKeyboardMarkup
import logging
from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

async def help(update, context):
    await update.message.reply_text(
        "Я бот справочник.")


async def address(update, context):
    await update.message.reply_text(
        "Адрес: г. Москва, ул. Льва Толстого, 16")


async def phone(update, context):
    await update.message.reply_text("Телефон: +7(495)776-3030")


async def site(update, context):
    await update.message.reply_text(
        "Сайт: http://www.yandex.ru/company")


async def work_time(update, context):
    await update.message.reply_text(
        "Время работы: круглосуточно.")


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("address", address))
    application.add_handler(CommandHandler("phone", phone))
    application.add_handler(CommandHandler("site", site))
    application.add_handler(CommandHandler("work_time", work_time))
    application.add_handler(CommandHandler("help", help))
    application.run_polling()

async def echo(update, context):
    print(update.message.text)
    print('id: ' + str(update.message.from_user.id) + '; username: ' +
          str(update.message.from_user.username) + '; name: ' + str(update.message.from_user.first_name) + ' ' +
          str(update.message.from_user.last_name) + ' -> ' + str(update.message.text))
    checkingAvailability(update.message.text)

    await update.message.reply_text(update.message.text)


def main():
    application = Application.builder().token("5381154310:AAHGvmHoo6StoC8_UpcIjZ8bWt4rVAccdzs").build()

    text_handler = MessageHandler(filters.TEXT, echo)

    application.add_handler(text_handler)

    application.run_polling()


if __name__ == '__main__':
    main()