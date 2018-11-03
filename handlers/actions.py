from handlers import create_button
import main 

handler_reply_button = [
    {
        'name': 'Разблокировать',
        'run': main.CheckUnlockPassword,
        'text': 'Авторизируйся в jira'
    },
    {
        'name': 'Авторизоваться',
        'run': create_button.serverBtn,
        'text': 'Выбери сервер'
    },
    {
        'name': 'Jira Software',
        'run': main.getServer,
        'text': 'Введи логин и пароль через пробел(user 1234), нажми Enter и потом уже нажимай на кнокпу Войти'
    },
    {
        'name': 'Puzanov Production',
        'run': main.getServer,
        'text': 'Введи логин и пароль через пробел(user 1234), нажми Enter и потом уже нажимай на кнокпу Войти'
    },
    {
        'name': 'Войти',
        'run': main.getloginPassword,
        'text': 'Пока генерируется данные только для проекта NappyClub'
    },
    {
        'name': 'Выйти',
        'run': create_button.auth_jira,
        'text': 'Заходи если что...'
    },
    {
        'name': 'Сгенерировать StandUp',
        'run': main.showProjects,
        'text': 'Список проектов, в которых ты вчера логал время'
    }
]

handler_inline_button = [
    {
        'name': '',
        'run': '',
        'text': ''
    }
]
