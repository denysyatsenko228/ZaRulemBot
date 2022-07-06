import abc
from markup.markup import Keyboards
from data_base.dbalchemy import DBManager


class Handler(metaclass=abc.ABCMeta):

    def __init__(self, bot):
        #  receiving of bots object
        self.bot = bot
        #  initializing of button layout
        self.keyboards = Keyboards()
        # initializing of manager for work with DB
        self.DB = DBManager()

    @abc.abstractmethod
    def handle(self):
        pass

