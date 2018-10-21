import logging
from handlers.parser_jira import generateStandup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler


_UPDATER = Updater("")

logging.basicConfig(level=logging.DEBUG, \
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Start function
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Бот для генерирования стендапов")

def standup(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Обработка данных...")
    bot.send_message(chat_id=update.message.chat_id, text="%s" % generateStandup())

# handler send command(=> /start <=)
_UPDATER.dispatcher.add_handler(CommandHandler('start', start))

# handler send command(=> /standup <=)
_UPDATER.dispatcher.add_handler(CommandHandler('standup', standup))

_UPDATER.start_polling()
_UPDATER.idle()