from handlers import messages, create_button


class Messages:

    def __init__(self):
        self.data = {}
        self.btn_callback_msg  = ''
        self._MESSAGE = 'self'

    def start(self, bot, update):
        self.data = {
            'bot': bot,
            'update': update
        }
        create_button.unlock(self.data)
    
    def listenSentMessages(self, array, message):
        for item in array:
            if (item['name'] == message):
                return item
        return None

    def message_processing(self, bot, update):
        self.btn_callback_msg = update._effective_message.text
        # action = self.listenSentMessages(messages.handler_reply_button, self.btn_callback_msg)
        # if (action != None):
        #     self._MESSAGE = self.btn_callback_msg
        #     self.run()
        # else:
        #     self._MESSAGE = update._effective_message.text
        #     self.run()
        if update._effective_message.text == 'Jira Software':
            self._MESSAGE = self.btn_callback_msg
            self.run()
        if update._effective_message.text == 'Puzanov Production':
            self._MESSAGE = self.btn_callback_msg
            self.run()
        if update._effective_message.text == 'Войти':
            self.run()
        if update._effective_message.text == 'Разблокировать':
            self.run()
        else:
            self._MESSAGE = update._effective_message.text
            self.run()

    def run(self):
        for item in range(len(messages.handler_reply_button)):
            if self.btn_callback_msg == messages.handler_reply_button[item]['name']:
                self.data.update({ 'item': item, 'message': self._MESSAGE })
                run = messages.handler_reply_button[item]['run']
                run(self.data)
