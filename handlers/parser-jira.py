from jira import JIRA
import datetime


jira = JIRA(basic_auth=("", ""), options={'server': 'https://nappyclub.atlassian.net'})

def getWorklogs(issues):
    worklogs = []
    for issue in issues:
        worklogs.append(jira.issue(str(issue.key)))
    return worklogs

def getYesterday():
    now = datetime.datetime.now()
    return "%d/%d/%d" % (now.year, now.month, now.day - 1)

def getYesterdayWorklogIssues():
    yesterday_issues_worklogs = jira.search_issues('worklogAuthor = currentUser() AND worklogDate = "%s"' % getYesterday())
    return getWorklogs(yesterday_issues_worklogs)
