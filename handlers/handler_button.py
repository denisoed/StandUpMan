from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from handlers.actions import handler_inline_button


# Handler click inline button
def button_processing(bot, update):
    query = update.callback_query.data
    for item in range(len(handler_inline_button)):
        if query == handler_inline_button[item]['name']:
            data.update({ 'bot': bot, 'update': update, 'message': handler_inline_button[item]['name'] })
            run = handler_inline_button[item]['run']
            run(data)