from telebot import TeleBot
from settings import config
from handlers.handler_main import HandlerMain


class TelBot:

    __version__ = config.VERSION
    __author__ = config.AUTHOR

    def __init__(self):
        self.token = config.TOKEN
        self.bot = TeleBot(self.token)
        self.handler = HandlerMain(self.bot)

    def start(self):
        #  обработка старта событий
        self.handler.handle()

    def run_bot(self):
        # обработка событий
        self.start()
        # служит для запуска бота
        self.bot.polling(none_stop=True)


if __name__ == '__main__':
    bot = TelBot()
    bot.run_bot()

