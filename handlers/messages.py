from handlers import create_button
from handlers.parser_jira import ParserJira
from main import CheckUnlockPassword

jira = ParserJira()

desc = {
    'start_msg': '''
Введи пароль!
''',
    'welcome': '''
Долго пишешь стендап? Грачуешь, когда собираешь в список то, что делал вчера?\n
Пиши нормальные ворлоги и я за тебя сформирую список того, что ты делал вчера.
'''
}

server = {
    'PuzanovProduction': {
        'statuses': ['В работе', 'For Development', 'Сделать', 'Selected for Development']
    },
    'JiraSoftware': {
        'statuses': ['Open', 'In Progress', 'Accepted', 'Idle']
    }
}

handler_reply_button = [
    {
        'name': 'Разблокировать',
        'run': CheckUnlockPassword,
        'text': 'Авторизируйся в jira'
    },
    {
        'name': 'Авторизоваться',
        'run': create_button.serverBtn,
        'text': 'Выбери сервер'
    },
    {
        'name': 'Jira Software',
        'run': jira.getServer,
        'text': 'Введи логин и пароль через пробел(user 1234), нажми Enter и потом уже нажимай на кнокпу Войти'
    },
    {
        'name': 'Puzanov Production',
        'run': jira.getServer,
        'text': 'Введи логин и пароль через пробел(user 1234), нажми Enter и потом уже нажимай на кнокпу Войти'
    },
    {
        'name': 'Войти',
        'run': jira.getloginPassword,
        'text': 'Пока генерируется данные только для проекта NappyClub'
    },
    {
        'name': 'Выйти',
        'run': create_button.auth_jira,
        'text': 'Заходи если что...'
    },
    {
        'name': 'Сгенерировать StandUp',
        'run': jira.showProjects,
        'text': 'Список проектов, в которых ты вчера логал время'
    }
]

handler_inline_button = [
    {
        'name': 'yet',
        'run': 'main.get_all_mentors',
        'text': 'yet'
    }
]
