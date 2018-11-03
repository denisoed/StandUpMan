from secrets import PASSWORD
from handlers import create_button
from api.Jira_api import JiraAPI

jira = JiraAPI()

def CheckUnlockPassword(data):
    if (data['message'] == PASSWORD):
        return data['bot'].send_message(chat_id=data['update'].message.chat_id, \
            reply_markup=create_button.auth_jira(data))
    else:
        return data['bot'].send_message(chat_id=data['update'].message.chat_id, \
            reply_markup=create_button.unlock(data))

def getServer(data):
    if data['message'] == 'Jira Software':
        jira.get_server('https://nappyclub.atlassian.net')
    elif data['message'] == 'Puzanov Production':
        jira.get_server('https://pm.maddevs.co')
    data['bot'].send_message(chat_id=data['update'].message.chat_id, \
        reply_markup=create_button.auth(data))

def getloginPassword(data):
    if data['message'] == 'Jira Software' or data['message'] == 'Puzanov Production':
            data['bot'].sendMessage(chat_id=data['update'].message.chat_id, \
                text='Логин и пароль через пробел!')
    else:
        array = data['message'].split(' ')
        logPass_array = ' '.join(array).split()
        if len(logPass_array) == 2:
            login = logPass_array[0]
            password = logPass_array[1]
            data['bot'].sendMessage(chat_id=data['update'].message.chat_id, text='Ожидай...')
            jira.auth_in_jira(login, password)
            data['bot'].send_message(chat_id=data['update'].message.chat_id, \
                reply_markup=create_button.generateStandup(data))
        else:
            data['bot'].sendMessage(chat_id=data['update'].message.chat_id, \
                text='Логин и пароль через пробел!')

def generateStandup(data):
    data['bot'].sendMessage(chat_id=data['update'].message.chat_id, text='Обработка данных...')
    standup = jira.generate_standup()
    data['bot'].sendMessage(chat_id=data['update'].message.chat_id, text=standup)