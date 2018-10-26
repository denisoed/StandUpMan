from handlers import create_button
from handlers.parser_jira import ParserJira

jira = ParserJira()

desc = {
    'start_msg': '''
Долго пишешь стендап? Грачуешь, когда собираешь в список то, что делал вчера?\n
Пиши нормальные ворлоги и я за тебя сформирую список того, что ты делал вчера.
'''
}

handler_reply_button = [
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
        'run': create_button.start_buttons,
        'text': 'Заходи если что...'
    },
    {
        'name': 'Сгенерировать StandUp',
        'run': jira.generateStandup,
        'text': 'Стендап готов!'
    }
]

handler_inline_button = [
    {
        'name': 'yet',
        'run': 'main.get_all_mentors',
        'text': 'yet'
    }
]
