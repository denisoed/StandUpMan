from data import messages
from handlers import actions
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

# Unlock bot
def unlock(data):
    unlock_btn = InlineKeyboardButton(text="Разблокировать")
    keyboard = [[unlock_btn]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    send = data['bot'].sendMessage(chat_id=data['update'].message.chat_id,
                           text=messages.desc['start_msg'], reply_markup=reply_markup)
    return send

# Auth in JIRA
def auth_jira(data):
    auth_btn = InlineKeyboardButton(text="Авторизоваться")
    help_me = InlineKeyboardButton(text="Помощь")
    keyboard = [[auth_btn], [help_me]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    send = data['bot'].sendMessage(chat_id=data['update'].message.chat_id,
                           text=messages.desc['welcome'], reply_markup=reply_markup)
    return send

# Server buttons
def serverBtn(data):
    blue_jira = InlineKeyboardButton(text="Jira Software")
    red_jira = InlineKeyboardButton(text="Puzanov Production")
    keyboard = [[blue_jira, red_jira]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    send = data['bot'].sendMessage(chat_id=data['update'].message.chat_id,
        text=actions.handler_reply_button[data['item']]['text'], reply_markup=reply_markup)
    return send

# Authorization
def auth(data):
    sign_in = InlineKeyboardButton(text="Войти")
    keyboard = [[sign_in]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    send = data['bot'].sendMessage(chat_id=data['update'].message.chat_id,
        text=actions.handler_reply_button[data['item']]['text'], reply_markup=reply_markup)
    return send

# Generate standup 
def generateStandup(data):
    standup = InlineKeyboardButton(text="Сгенерировать StandUp")
    sign_out = InlineKeyboardButton(text="Выйти")
    keyboard = [[standup], [sign_out]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    send = data['bot'].sendMessage(chat_id=data['update'].message.chat_id,
        text=actions.handler_reply_button[data['item']]['text'], reply_markup=reply_markup)
    return send

# Projects list button
def projectsButton(data):
    keyboard = []
    counter = 0
    tempArray = []
    for project in data['projects']:
        button = InlineKeyboardButton(text="{name}".format(name=project['name']))
        if (counter == 2):
            counter = 0
            keyboard.append(tempArray)
            tempArray = []
            tempArray.append(button)
            counter += 1
        else:
            tempArray.append(button)
            counter += 1
    if (tempArray != []):
        keyboard.append(tempArray)
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    send = data['bot'].sendMessage(chat_id=data['update'].message.chat_id,
        text=actions.handler_reply_button[data['item']]['text'], reply_markup=reply_markup)
    return send
