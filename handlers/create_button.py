from handlers import messages
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

# Start button
def start_buttons(bot, update, item, message):
    auth_btn = InlineKeyboardButton(text="Авторизоваться")
    keyboard = [[auth_btn]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    send = bot.sendMessage(chat_id=update.message.chat_id,
                           text='Для начала давай авторизуемся', reply_markup=reply_markup)
    return send

# Server buttons
def serverBtn(bot, update, item, message):
    blue_jira = InlineKeyboardButton(text="Jira Software")
    red_jira = InlineKeyboardButton(text="Puzanov Production")
    keyboard = [[blue_jira, red_jira]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    send = bot.sendMessage(chat_id=update.message.chat_id,
                           text='Выбери сервер', reply_markup=reply_markup)
    return send

# Authorization
def auth(bot, update, item, message):
    sign_in = InlineKeyboardButton(text="Войти")
    keyboard = [[sign_in]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    send = bot.sendMessage(chat_id=update.message.chat_id,
                           text='Введи логин и пароль через пробел > login password, нажми Enter и потом уже нажимай на кнокпу Войти', reply_markup=reply_markup)
    return send

# Generate standup 
def generateStandup(bot, update, item, message):
    standup = InlineKeyboardButton(text="Сгенерировать StandUp")
    sign_out = InlineKeyboardButton(text="Выйти")
    keyboard = [[standup], [sign_out]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    send = bot.sendMessage(chat_id=update.message.chat_id,
                           text='Пока генерируется данные только для блока ВЧЕРА', reply_markup=reply_markup)
    return send
