from jira import JIRA
import datetime
from telegram import ParseMode
from handlers import create_button



class ParserJira:
    """docstring"""

    def __init__(self, server=None, login=None, password=None, jira=None):
        self.server = server
        self.login = login
        self.password = password
        self.jira = jira


    def authInJira(self, bot, update, item, message):
        bot.sendMessage(chat_id=update.message.chat_id, text='Ожидай...')
        self.jira = JIRA(basic_auth=('{0}'.format(self.login), '{0}'.format(self.password)), options={'server': '{0}'.format(self.server)})
        bot.send_message(chat_id=update.message.chat_id, \
            reply_markup=create_button.generateStandup(bot, update, item, message))

    def getServer(self, bot, update, item, message):
        if message == 'Jira Software':
            self.server = 'https://nappyclub.atlassian.net'
        elif message == 'Puzanov Production':
            self.server = 'https://pm.maddevs.co'
        bot.send_message(chat_id=update.message.chat_id, \
            reply_markup=create_button.auth(bot, update, item, message))

    def getloginPassword(self, bot, update, item, message):
        if message == 'Jira Software' or message == 'Puzanov Production':
            bot.sendMessage(chat_id=update.message.chat_id, \
                text='Логин и пароль через пробел!')
        else:
            array = message.split(' ')
            logPass_array = ' '.join(array).split()
            if len(logPass_array) == 2:
                self.login = logPass_array[0]
                self.password = logPass_array[1]
                self.authInJira(bot, update, item, message)
            else:
                bot.sendMessage(chat_id=update.message.chat_id, \
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

    def getProjects():
        projects = self.jira.projects()
        return projects

    def getYesterdayWorklogIssues(self):
        yesterday_issues_worklogs = self.jira.search_issues('worklogAuthor = currentUser() AND worklogDate = "%s"' % self.getYesterday())
        return self.getWorklogs(yesterday_issues_worklogs)

    def getTodayIssues(self):
        today_issues = self.jira.search_issues('assignee = currentuser() AND project = "NappyClub" AND sprint in openSprints() AND worklogAuthor = currentUser() AND status in (Idle, Accepted, Open, "In Progress")')
        return today_issues

    def generateStandup(self, bot, update, item, message):
        bot.sendMessage(chat_id=update.message.chat_id, text='Обработка данных...')
        issues_with_worklogs = self.getYesterdayWorklogIssues()
        today_issues_with_worklogs = self.getTodayIssues()
        yesterday = ''
        today = ''
        for issue in issues_with_worklogs:
            yesterday += '- {0} {1}/browse/{2}\n'.format(self.handlerWorklogs(issue.fields.worklog.worklogs), self.server, issue.key)
            
        for issue in today_issues_with_worklogs:
            today += '- {0} {1}/browse/{2}\n'.format(issue.fields.summary, self.server, issue.key)
        
        standup = 'Доброе утро!\n\n*Вчера*\n{0}\n*Сегодня*\n{1}\n\n*Проблемы*\n{2}'.format(yesterday, today, '- Нет проблем!')
        bot.sendMessage(chat_id=update.message.chat_id, text=standup)
