from handlers import messages, create_button

# Necessary variables
_MESSAGE = 'test'

def start(bot, update):
    create_button.start_buttons( \
        bot, update, 0, 'Нужно авторизоваться')

# Handler incoming messages
def message_processing(bot, update):
    btn_callback_msg = update._effective_message.text
    if update._effective_message.text == 'Авторизоваться':
        run(bot, update, btn_callback_msg)
    if update._effective_message.text == 'Jira Software':
        global _MESSAGE
        _MESSAGE = btn_callback_msg
        run(bot, update, btn_callback_msg)
    if update._effective_message.text == 'Puzanov Production':
        _MESSAGE
        _MESSAGE = btn_callback_msg
        run(bot, update, btn_callback_msg)
    if update._effective_message.text == 'Войти':
        run(bot, update, btn_callback_msg)
    if update._effective_message.text == 'Выйти':
        run(bot, update, btn_callback_msg)
    else:
        _MESSAGE = update._effective_message.text
        run(bot, update, btn_callback_msg)

def run(bot, update, btn_callback_msg):
    for item in range(len(messages.handler_reply_button)):
        if btn_callback_msg == messages.handler_reply_button[item]['name']:
            run = messages.handler_reply_button[item]['run']
            run(bot, update, item, _MESSAGE)
