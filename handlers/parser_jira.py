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
        self.jira = JIRA(basic_auth=('{0}'.format(self.login), '{0}'.format(self.password)), options={'server': '{0}'.format(self.server)})
        bot.send_message(chat_id=update.message.chat_id, \
            reply_markup=create_button.generateStandup(bot, update, item, message))


    # authInJira('https://nappyclub.atlassian.net', 'denisod93@gmail.com', 'gorod312')

    def getServer(self, bot, update, item, message):
        if message == 'Jira Software':
            self.server = 'https://nappyclub.atlassian.net'
        elif message == 'Puzanov Production':
            self.server = 'https://pm.maddevs.co'
        bot.send_message(chat_id=update.message.chat_id, \
            reply_markup=create_button.auth(bot, update, item, message))

    def getloginPassword(self, bot, update, item, message):
        logPass = message.split(' ')
        self.login = logPass[0]
        self.password = logPass[1]
        self.authInJira(bot, update, item, message)

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
        yesterday_issues_worklogs = self.jira.search_issues('worklogAuthor = currentUser() AND worklogDate = "%s"' % self.getYesterday())
        return self.getWorklogs(yesterday_issues_worklogs)

    def generateStandup(self, bot, update, item, message):
        issues_with_worklogs = self.getYesterdayWorklogIssues()
        yesterday = ''
        for issue in issues_with_worklogs:
            yesterday += '- {0} https://nappyclub.atlassian.net/browse/{1}\n'.format(self.handlerWorklogs(issue.fields.worklog.worklogs), issue.key)

        standup = 'Доброе утро!\n\n*Вчера*\n%s\n*Сегодня*\n%s\n\n*Проблемы*\n%s' % (yesterday, '- Чинить баги', '- Нет проблем!')
        bot.sendMessage(chat_id=update.message.chat_id, text=standup)
        return standup
