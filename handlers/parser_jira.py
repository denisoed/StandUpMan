from jira import JIRA
import datetime
from telegram import ParseMode
import threading
from handlers import create_button



class ParserJira:
    """docstring"""

    def __init__(self, server=None, login=None, password=None, jira=None, userProjects=[], boardStatuses=[]):
        self.jira = jira
        self.server = server
        self.login = login
        self.password = password
        self.userProjects = userProjects
        self.boardStatuses = boardStatuses

    def getProjectsWithYesterdayWorklogs(self, project):
        issues = self.jira.search_issues('worklogAuthor = currentUser() AND project={key} AND worklogDate = {yesterday}'.format(key=project.key, yesterday=self.getYesterday()))
        if (issues != []):
            self.userProjects.append({'key': project.key, 'name': project.name})
    
    def getServerBoardStatuses(self):
        self.boardStatuses = self.jira.statuses()

    def getInfoUserProjects(self):
        threads = []
        allProjects = self.jira.projects()

        for project in allProjects:
            threads.append(threading.Thread(target=self.getProjectsWithYesterdayWorklogs, args=(project,)))
        
        for thread in threads:
            thread.start()

    def authInJira(self, data):
        data['bot'].sendMessage(chat_id=data['update'].message.chat_id, text='Ожидай...')
        self.jira = JIRA(basic_auth=('{0}'.format(self.login), '{0}'.format(self.password)), options={'server': '{0}'.format(self.server)}, max_retries=0)
        self.getServerBoardStatuses()
        self.getInfoUserProjects()
        data['bot'].send_message(chat_id=data['update'].message.chat_id, \
            reply_markup=create_button.generateStandup(data))

    def getServer(self, data):
        if data['message'] == 'Jira Software':
            self.server = 'https://nappyclub.atlassian.net'
        elif data['message'] == 'Puzanov Production':
            self.server = 'https://pm.maddevs.co'
        data['bot'].send_message(chat_id=data['update'].message.chat_id, \
            reply_markup=create_button.auth(data))

    def getloginPassword(self, data):
        if data['message'] == 'Jira Software' or data['message'] == 'Puzanov Production':
            data['bot'].sendMessage(chat_id=data['update'].message.chat_id, \
                text='Логин и пароль через пробел!')
        else:
            array = data['message'].split(' ')
            logPass_array = ' '.join(array).split()
            if len(logPass_array) == 2:
                self.login = logPass_array[0]
                self.password = logPass_array[1]
                self.authInJira(data)
            else:
                data['bot'].sendMessage(chat_id=data['update'].message.chat_id, \
                    text='Логин и пароль через пробел!')

    def getWorklogs(self, issues):
        worklogs = []
        for issue in issues:
            worklogs.append(self.jira.issue(str(issue.key)))
        return worklogs

    def handlerWorklogs(self, worklogs):
        yesterday = self.getYesterday()
        message = ''
        for worklog in worklogs:
            if yesterday == worklog.created[0:10]:
                message += '{0}({1}) '.format(worklog.comment.strip(), worklog.timeSpent)
        return message

    def getYesterday(self):
        now = datetime.datetime.now()
        if now.weekday() == 0:
            return "%d-%d-%d" % (now.year, now.month, now.day - 3)
        elif now.weekday() == 6:
            return "%d-%d-%d" % (now.year, now.month, now.day - 2)
        else:
            return "%d-%d-%d" % (now.year, now.month, now.day - 1)

    def getYesterdayWorklogIssues(self):
        yesterday_issues_worklogs = self.jira.search_issues('worklogAuthor = currentUser() AND worklogDate = "{yesterday}"'.format(yesterday=self.getYesterday()))
        return self.getWorklogs(yesterday_issues_worklogs)

    def getTodayIssues(self):
        today_issues = self.jira.search_issues('assignee = currentuser() AND project = "NappyClub" AND sprint in openSprints() AND worklogAuthor = currentUser() AND status in (Idle, Accepted, Open, "In Progress")')
        return today_issues

    def showProjects(self, data):
        data.update({ 'projects': self.userProjects })
        data['bot'].send_message(chat_id=data['update'].message.chat_id, \
            reply_markup=create_button.projectsButton(data))

    def generateStandup(self, data):
        data['bot'].sendMessage(chat_id=data['update'].message.chat_id, text='Обработка данных...')
        issues_with_worklogs = self.getYesterdayWorklogIssues()
        today_issues_with_worklogs = self.getTodayIssues()
        yesterday = ''
        today = ''
        for issue in issues_with_worklogs:
            yesterday += '- {0} {1}/browse/{2}\n'.format(self.handlerWorklogs(issue.fields.worklog.worklogs), self.server, issue.key)
            
        for issue in today_issues_with_worklogs:
            today += '- {0} {1}/browse/{2}\n'.format(issue.fields.summary, self.server, issue.key)
        
        standup = 'Доброе утро!\n\n*Вчера*\n{0}\n*Сегодня*\n{1}\n\n*Проблемы*\n{2}'.format(yesterday, today, '- Нет проблем!')
        data['bot'].sendMessage(chat_id=data['update'].message.chat_id, text=standup)
