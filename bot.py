import logging
from handlers.parser_jira import generateStandup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from handlers.handler_message import start, message_processing
from handlers.handler_button import button_processing

_UPDATER = Updater("")

logging.basicConfig(level=logging.DEBUG, \
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# handler send command(=> /start <=)
_UPDATER.dispatcher.add_handler(CommandHandler('start', start))

def standup(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Обработка данных...")
    bot.send_message(chat_id=update.message.chat_id, text="%s" % generateStandup())

# handler send command(=> /start <=)
_UPDATER.dispatcher.add_handler(CommandHandler('start', start))

# handler send command(=> /standup <=)
_UPDATER.dispatcher.add_handler(CommandHandler('standup', standup))

# handler send message
_UPDATER.dispatcher.add_handler(MessageHandler(Filters.text, message_processing))

# handler click button
# _UPDATER.dispatcher.add_handler(CallbackQueryHandler(button_processing))

_UPDATER.start_polling()
_UPDATER.idle()