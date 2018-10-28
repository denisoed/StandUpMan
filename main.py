from secrets import PASSWORD
from handlers import create_button

def CheckUnlockPassword(data):
    if (data['message'] == PASSWORD):
        data['bot'].send_message(chat_id=data['update'].message.chat_id, \
            reply_markup=create_button.auth_jira(data))
    else:
        data['bot'].send_message(chat_id=data['update'].message.chat_id, \
            reply_markup=create_button.unlock(data))
