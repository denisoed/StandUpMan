import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from handlers.handler_message import Messages
from handlers.handler_button import button_processing

_UPDATER = Updater("")

logging.basicConfig(level=logging.DEBUG, \
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler_messages = Messages()

# handler send command(=> /start <=)
_UPDATER.dispatcher.add_handler(CommandHandler('start', handler_messages.start))

# handler send message
_UPDATER.dispatcher.add_handler(MessageHandler(Filters.text, handler_messages.message_processing))

# handler click button
# _UPDATER.dispatcher.add_handler(CallbackQueryHandler(button_processing))

_UPDATER.start_polling()
_UPDATER.idle()