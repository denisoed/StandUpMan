from jira import JIRA
import datetime
from telegram import ParseMode
import threading
from handlers import create_button


class JiraAPI:
    """docstring"""

    def __init__(self, server=None, login=None, password=None, jira=None, userProjects=[], boardStatuses=[]):
        self.server = server
        self.login = login
        self.password = password
        self.jira = jira
        self.userProjects = userProjects
        self.boardStatuses = boardStatuses

    def get_projects_with_yesterday_worklogs(self, project):
        issues = self.jira.search_issues('worklogAuthor = currentUser() AND project={key} AND worklogDate = {yesterday}'.format(key=project.key, yesterday=self.get_yesterday()))
        if (issues != []):
            self.userProjects.append({'key': project.key, 'name': project.name})
        return self.userProjects
    
    def get_server_board_statuses(self):
        self.boardStatuses = self.jira.statuses()
        return self.boardStatuses

    def get_info_user_projects(self):
        threads = []
        allProjects = self.jira.projects()

        for project in allProjects:
            threads.append(threading.Thread(target=self.get_projects_with_yesterday_worklogs, args=(project,)))
        
        for thread in threads:
            thread.start()

    def auth_in_jira(self, login, password):
        self.jira = JIRA(basic_auth=('{0}'.format(login), '{0}'.format(password)), options={'server': '{0}'.format(self.server)}, max_retries=0)
        self.get_server_board_statuses()
        self.get_info_user_projects()

    def get_server(self, server):
        self.server = server
        return server

    def get_worklogs(self, issues):
        worklogs = []
        for issue in issues:
            worklogs.append(self.jira.issue(str(issue.key)))
        return worklogs

    def handler_worklogs(self, worklogs):
        yesterday = self.get_yesterday()
        message = ''
        for worklog in worklogs:
            if yesterday == worklog.created[0:10]:
                message += '{0}({1}). '.format(worklog.comment.strip(), worklog.timeSpent)
        return message

    def get_yesterday(self):
        today = datetime.date.today()
        if today.weekday() == 0:
            return str(today - datetime.timedelta(days=3))
        elif today.weekday() == 6:
            return str(today - datetime.timedelta(days=2))
        else:
            return str(today - datetime.timedelta(days=5))

    def get_yesterday_worklog_issues(self):
        yesterday_issues_worklogs = self.jira.search_issues('worklogAuthor = currentUser() AND worklogDate = "{yesterday}"'.format(yesterday=self.get_yesterday()))
        return self.get_worklogs(yesterday_issues_worklogs)

    def get_today_issues(self):
        today_issues = self.jira.search_issues('assignee = currentuser() AND project = "NappyClub" AND sprint in openSprints() AND worklogAuthor = currentUser() AND status in (Idle, Accepted, Open, "In Progress")')
        return today_issues

    def show_projects(self):
        return self.userProjects
    
    def get_projects(self):
        return self.userProjects

    def generate_standup(self):
        issues_with_worklogs = self.get_yesterday_worklog_issues()
        today_issues_with_worklogs = self.get_today_issues()
        yesterday = ''
        today = ''
        for issue in issues_with_worklogs:
            yesterday += '- {0} {1}/browse/{2}\n'.format(self.handler_worklogs(issue.fields.worklog.worklogs), self.server, issue.key)
            
        for issue in today_issues_with_worklogs:
            today += '- {0} {1}/browse/{2}\n'.format(issue.fields.summary, self.server, issue.key)
        
        standup = 'Доброе утро!\n\n*Вчера*\n{0}\n*Сегодня*\n{1}\n\n*Проблемы*\n{2}'.format(yesterday, today, '- Нет проблем!')
        return standup
