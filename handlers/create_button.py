from handlers import messages
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

# Start button
def start_buttons(bot, update, item, message):
    auth_btn = InlineKeyboardButton(text="Авторизоваться")
    keyboard = [[auth_btn]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    send = bot.sendMessage(chat_id=update.message.chat_id,
                           text=message, reply_markup=reply_markup)
    return send

# Authorization
def auth(bot, update, item, message):
    sign_in = InlineKeyboardButton(text="Войти")
    keyboard = [[sign_in]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    send = bot.sendMessage(chat_id=update.message.chat_id,
                           text=message, reply_markup=reply_markup)
    return send

# Generate standup 
def generateStandup(bot, update, item, message):
    sign_in = InlineKeyboardButton(text="Сгенерировать StandUp")
    keyboard = [[sign_in]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    send = bot.sendMessage(chat_id=update.message.chat_id,
                           text=message, reply_markup=reply_markup)
    return send
