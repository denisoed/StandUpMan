from handlers import create_button
from handlers.parser_jira import ParserJira

jira = ParserJira()

handler_reply_button = [
    {
        'name': 'Авторизоваться',
        'run': create_button.serverBtn,
        'text': 'Привет'
    },
    {
        'name': 'Jira Software',
        'run': jira.getServer,
        'text': 'sdsdsd'
    },
    {
        'name': 'Puzanov Production',
        'run': jira.getServer,
        'text': 'test'
    },
    {
        'name': 'Войти',
        'run': jira.getloginPassword,
        'text': 'test'
    },
    {
        'name': 'Выйти',
        'run': create_button.start_buttons,
        'text': 'test'
    },
    {
        'name': 'Сгенерировать StandUp',
        'run': jira.generateStandup,
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
