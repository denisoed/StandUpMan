from handlers import messages
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

# Start button
def start_buttons(data):
    auth_btn = InlineKeyboardButton(text="Авторизоваться")
    keyboard = [[auth_btn]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    send = data['bot'].sendMessage(chat_id=data['update'].message.chat_id,
                           text=messages.desc['start_msg'], reply_markup=reply_markup)
    return send

# Server buttons
def serverBtn(data):
    blue_jira = InlineKeyboardButton(text="Jira Software")
    red_jira = InlineKeyboardButton(text="Puzanov Production")
    keyboard = [[blue_jira, red_jira]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    send = data['bot'].sendMessage(chat_id=data['update'].message.chat_id,
        text=messages.handler_reply_button[data['item']]['text'], reply_markup=reply_markup)
    return send

# Authorization
def auth(data):
    sign_in = InlineKeyboardButton(text="Войти")
    keyboard = [[sign_in]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    send = data['bot'].sendMessage(chat_id=data['update'].message.chat_id,
        text=messages.handler_reply_button[data['item']]['text'], reply_markup=reply_markup)
    return send

# Generate standup 
def generateStandup(data):
    standup = InlineKeyboardButton(text="Сгенерировать StandUp")
    sign_out = InlineKeyboardButton(text="Выйти")
    keyboard = [[standup], [sign_out]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    send = data['bot'].sendMessage(chat_id=data['update'].message.chat_id,
        text=messages.handler_reply_button[data['item']]['text'], reply_markup=reply_markup)
    return send

# Generate standup 
def projectsButton(data):
    keyboard = []
    for key in data['keys']:
        button = InlineKeyboardButton(text="{key}".format(key=key))
        keyboard.append([button])
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    send = data['bot'].sendMessage(chat_id=data['update'].message.chat_id,
        text=messages.handler_reply_button[data['item']]['text'], reply_markup=reply_markup)
    return send
