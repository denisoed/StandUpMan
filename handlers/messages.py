from handlers import create_button
from handlers import parser_jira

handler_reply_button = [
    {
        'name': 'Авторизоваться',
        'run': create_button.auth,
        'text': 'test'
    },
    {
        'name': 'Войти',
        'run': create_button.generateStandup,
        'text': 'test'
    },
    {
        'name': 'Сгенерировать StandUp',
        'run': parser_jira.generateStandup,
        'text': 'test'
    }
]

handler_inline_button = [
    {
        'name': 'yet',
        'run': 'main.get_all_mentors',
        'text': 'yet'
    }
]
