import os
from emoji import emojize


TOKEN = '5543188791:AAHvnIPsITbSpbOnaDZ5ipqb38r6NofrBYE'

NAME_DB = 'products.sqlite'

VERSION = '0.0.1'

AUTHOR = 'denysyatsenko'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join('sqlite:///' + BASE_DIR, NAME_DB)

COUNT = 0

KEYBOARD = {
    'CHOOSE_GOODS': emojize(':open_file_folder: Выбрать товар'),
    'INFO': emojize(':speech_balloon: О магазине'),
    'SETTINGS': emojize(':⚙ Настройки'),
    'AUTO_CHEMISTRY': emojize(':bubbles: Масла, жидкости, автохимия'),
    'AUTO_PARTS': emojize(':automobile: Автозапчасти'),
    'AUDIO_AND_ELECTRONICS': emojize(':muted_speaker: Аудио и электроника'),
    '<<': emojize('⏪'),
    '>>': emojize('⏩'),
    'BACK_STEP': emojize('◀️'),
    'NEXT_STEP': emojize('▶️'),
    'ORDER': emojize('✅ ЗАКАЗ'),
    'X': emojize('❌'),
    'DOUWN': emojize('🔽'),
    'AMOUNT_PRODUCT': COUNT,
    'AMOUNT_ORDERS': COUNT,
    'UP': emojize('🔼'),
    'APPLY': '✅ Оформить заказ',
    'COPY': '©️ Denys Yatsenko'
}

CATEGORY = {
    'AUTO_CHEMISTRY': 1,
    'AUTO_PARTS': 2,
    'AUDIO_AND_ELECTRONICS': 3,
}

COMMANDS = {
    'START': "start",
    'HELP': "help",
}
