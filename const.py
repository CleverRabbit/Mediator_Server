from bot_config import BOT_TOKEN, BOT_ID, GROUP_ID, BROADCAST_ID

# порт api сервера медиатора
SERVER_PORT = 5010

# порты api клиентов медиатора
CLIENT_PORTS = {
    'tg': 5011,
    'vk': 5012,
}

# если нужны бекапы, и восстановление, то True
NEED_BACKUP = True

# текстовики
GREETING_TEXT = 'Приветствуем! Мы ответим Вам при первой возможности.'
ABON_GOT_TEXT = 'Абоненту отправлено сообщение:\n\n{text}'
CREATING_LOG = 'Топик "{topic}" (#{social}) создан'
CLOSING_LOG = '{name} закрыл топик "{topic}"'
BANNING_LOG = '{name} забанил абонента "{topic}"'
UNBANNING_LOG = '{name} разбанил абонента "{topic}"'
BROADCAST_LOG = '{name}\n\nвсем ожидающим:\n\n{text}'
POST_ERROR_LOG = 'Mediator_{social} помер (или притворяется):\n{error}'

ABON_BAN_TEXT = '''
Уважаемый абонент! В данный момент для Вас заблокирована возможность писать сообщения. Обратитесь пожалуйста в нашу службу технической поддержки:

206 - для абонентов-физических лиц
207 - для корпоративных абонентов
'''


# цвета иконок при создании топика
ICON_COLORS = {
    'magenta': 13338331,
    'yellow': 16766590,
    'green': 9367192,
    'pink': 16749490,
    'blue': 7322096,
    'red': 16478047,
}

# соответствия цветов соц.сетям
SOCIAL_COLORS = {
    'tg': ICON_COLORS['magenta'],
    'vk': ICON_COLORS['blue'],
}

# цвета в названиях топиков
STATE_COLORS = {
    'closed': 'red',
    'answered': 'yellow',
    'opened': 'green',
    'banned': 'black',
}
