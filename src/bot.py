import telebot


class Bot:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id
        self.bot = telebot.TeleBot(self.token)

    def send_message(self, message):
        self.bot.send_message(chat_id=self.chat_id, text=message)

