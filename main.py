from secrets import PASSWORD
from handlers import create_button
from data import messages
from api.Jira_api import JiraAPI

jira = JiraAPI()

# Send mesasge to telegram
def sendMessage(data, text):
    data['bot'].sendMessage(chat_id=data['update'].message.chat_id, text=text)

def sendButtons(data, buttons):
    data['bot'].send_message(chat_id=data['update'].message.chat_id, \
        reply_markup=buttons)

def defineMessage(data, message):
    userProjects = jira.show_projects()
    for project in userProjects:
        if project['name'] == message:
            server = jira.get_server()
            data.update({
                'project': message,
                'statuses': messages.servers[server]['statuses']
            })
            generateStandup(data)
            return message

# Generate StandUp
def CheckUnlockPassword(data):
    if (data['message'] == PASSWORD):
        return sendButtons(data, create_button.auth_jira(data))
    else:
        return sendButtons(data, create_button.unlock(data))

def getServer(data):
    if data['message'] == 'Jira Software':
        jira.set_server('https://nappyclub.atlassian.net')
    elif data['message'] == 'Puzanov Production':
        jira.set_server('https://pm.maddevs.co')
    return sendButtons(data, create_button.auth(data))

def getloginPassword(data):
    if data['message'] == 'Jira Software' or data['message'] == 'Puzanov Production':
        return sendMessage(data, 'Логин и пароль через пробел!')
    else:
        array = data['message'].split(' ')
        logPass_array = ' '.join(array).split()
        if len(logPass_array) == 2:
            login = logPass_array[0]
            password = logPass_array[1]
            sendMessage(data, 'Ожидай...')
            jira.auth_in_jira(login, password)
            return sendButtons(data, create_button.generateStandup(data))
        else:
            return sendMessage(data, 'Логин и пароль через пробел!')

def showProjects(data):
    userProjects = jira.show_projects()
    data.update({ 'projects': userProjects })
    return sendButtons(data, create_button.projectsButton(data))

def generateStandup(data):
    sendMessage(data, 'Обработка данных...')
    standup = jira.generate_standup(data)
    return sendMessage(data, standup)