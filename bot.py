import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler


_UPDATER = Updater("")

logging.basicConfig(level=logging.DEBUG, \
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Start function
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

# handler send command(=> /start <=)
_UPDATER.dispatcher.add_handler(CommandHandler('start', start))

_UPDATER.start_polling()
_UPDATER.idle()