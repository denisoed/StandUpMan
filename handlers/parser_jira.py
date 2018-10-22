from jira import JIRA
import datetime
from telegram import ParseMode


jira = JIRA(basic_auth=("", ""), options={'server': 'https://pm.maddevs.co'})
# def authInJira():
#     jira = JIRA(basic_auth=("", ""), options={'server': 'https://nappyclub.atlassian.net'})
#     return jira

def getWorklogs(issues):
    worklogs = []
    for issue in issues:
        worklogs.append(jira.issue(str(issue.key)))
    return worklogs

def handlerWorklogs(worklogs):
    yesterday = getYesterday()
    message = ''
    for worklog in worklogs:
        if yesterday == worklog.created[0:10]:
            message += '{0}({1}) '.format(worklog.comment.strip(), worklog.timeSpent)
    return message

def getYesterday():
    now = datetime.datetime.now()
    if now.weekday() == 0:
        return "%d-%d-%d" % (now.year, now.month, now.day - 3)
    elif now.weekday() == 6:
        return "%d-%d-%d" % (now.year, now.month, now.day - 2)
    else:
        return "%d-%d-%d" % (now.year, now.month, now.day - 1)

def getYesterdayWorklogIssues():
    yesterday_issues_worklogs = jira.search_issues('worklogAuthor = currentUser() AND worklogDate = "%s"' % getYesterday())
    return getWorklogs(yesterday_issues_worklogs)

def generateStandup(bot, update, item, message):
    issues_with_worklogs = getYesterdayWorklogIssues()
    yesterday = ''
    for issue in issues_with_worklogs:
        yesterday += '- {0} https://nappyclub.atlassian.net/browse/{1}\n'.format(handlerWorklogs(issue.fields.worklog.worklogs), issue.key)

    standup = 'Доброе утро!\n\n*Вчера*\n%s\n*Сегодня*\n%s\n\n*Проблемы*\n%s' % (yesterday, '- Чинить баги', '- Нет проблем!')
    bot.sendMessage(chat_id=update.message.chat_id, text=standup)
    return standup
