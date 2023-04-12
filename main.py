import json
import logging
from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler

""""5381154310:AAHGvmHoo6StoC8_UpcIjZ8bWt4rVAccdzs"""



# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def readingNotifications(update, context):
    print('id: ' + str(update.message.from_user.id) + '; username: ' +
          str(update.message.from_user.username) + '; name: ' + str(update.message.from_user.first_name) + ' ' +
          str(update.message.from_user.last_name) + ' -> ' + str(update.message.text))

    premium = (str(update.message.from_user.id) +
               str(update.message.from_user.username) +
               str(update.message.from_user.first_name) +
               str(update.message.from_user.last_name)
               )

    await update.message.reply_text(checkingAvailability(update.message.text, premium))


def main():
    application = Application.builder().token("5381154310:AAHGvmHoo6StoC8_UpcIjZ8bWt4rVAccdzs").build()

    text_handler = MessageHandler(filters.TEXT, readingNotifications)

    application.add_handler(text_handler)

    application.run_polling()


def checkingForPremium(message):
    f = open("CashUsers.txt", "r", encoding="utf8")
    lines = [elem.strip() + "" for elem in f.readlines()]
    f.close()
    for elem in lines:
        if elem == message:
            return True
    return False


def checkingAvailability(text, premium):
    if text in free_db.keys():
        return free_db[text]
    elif text in cash_db.keys() and checkingForPremium(premium):
        return cash_db[text]
    elif text in cash_db.keys():
        return "Ой-ой-ой, похоже, решение этой задачи доступно только с премиум аккаунтом"
    elif text == "/start":
        return """
Салам Алейкум. Это бот, который решает задачи яндекс лицея первого года обученя. Чтобы узнать как работает бот, пиши /help
Поскольку решение задач - являние времязатратное, в нашем боте доступны не все решения. Чтобы разблокировать полный доступ, пиши /vip"""

    elif text == "/help":
        return """ 
Чтобы узнать решение задачи ЯЛ первого года, необходимол написать её название в чат с этим ботом.
остались вопросы -> @glortest"""

    elif text == "/vip":
        print("PREMIUM: " + premium)
        return """
Друг, ты ступил на путь истины, на путь 80ти баллов за первый год обучения, написав эту команду. 
Для полной разблокировки бота необходимо - перевести N рублей на номер +N(NNN)NNN-NN-NN по СБП. 
После оплаты в чат бота напиши такое сообщение: /+N(), поместив внутрь скобок свой номер телефона. 
Потом придётся подожди нексколько минут, а затем наслаждаться жизнью, ведь не придётся ботать ЯЛ"""

    elif text[:4] == "/+N(":
        filep = open("Request.txt", "w", encoding="utf8")
        filep.writelines(premium + " " + text[4:-1])
        return "Теперь придётся немного подождать, уже обрабатываем вашу заявку"

    elif text == "/startDebugModeLoginGlortestParol14881488":
        f = open("Request.txt", "r", encoding="utf8")
        lines = [elem.strip() + "" for elem in f.readlines()]
        sj = str("\n".join(lines))
        return sj

    elif text == "/DebugModeLoginGlortestParol14881488ClearAllR":
        open('Request.txt', 'w').close()
        return "OK"

    else:
        return "похоже, вы ошиблись и не правильно ввели текст"




if __name__ == '__main__':
    with open('db_cash.json') as filej:
        cash_db = json.load(filej)
    with open('db_free.json') as filej:
        free_db = json.load(filej)
    main()
