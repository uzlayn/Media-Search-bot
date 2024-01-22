import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'BQC6kfsAVd4ZkiWtMz_lW9BZNEYD_jfxtBTPSsnrZcywz6TZFr4WhbSLpkeULtwhR4jYwNoQ_HazMpPD3TNM-AZOX9KeexKPQfZMtd_oL-GPOx8TW0E3prFAYgNm6bXoxTgsQufE0vK7ASFdzDqhf9jF8asnR97m339DzcOlQwXBUqc-BpLWHYhNuipD32jTv5eTfD3ie6zvG7oqQmkLsvP5oAspNbrwXn9oFvzNrrJtZyCpZvaNDFUPWHifpbCkXiLbqxnoOusN7RInRfGnAbxM9e8W7qRvtA7dpJqTBLHYSlkxMGp36r0qG1e6aDGxLz0dsTQbF5AuCdy9KS7qhWAqS9I8nQAAAAFa5ESRAA')
API_ID = int(environ['25336929'])
API_HASH = environ['308f4c34a6c3b90a74546d7e7e3087c2']
BOT_TOKEN = environ['6705541825:AAGVNZE9qUtTVyfMe0_m4aL06L1EGHjLli8']
USERBOT_STRING_SESSION = environ.get('BQC6kfsAVd4ZkiWtMz_lW9BZNEYD_jfxtBTPSsnrZcywz6TZFr4WhbSLpkeULtwhR4jYwNoQ_HazMpPD3TNM-AZOX9KeexKPQfZMtd_oL-GPOx8TW0E3prFAYgNm6bXoxTgsQufE0vK7ASFdzDqhf9jF8asnR97m339DzcOlQwXBUqc-BpLWHYhNuipD32jTv5eTfD3ie6zvG7oqQmkLsvP5oAspNbrwXn9oFvzNrrJtZyCpZvaNDFUPWHifpbCkXiLbqxnoOusN7RInRfGnAbxM9e8W7qRvtA7dpJqTBLHYSlkxMGp36r0qG1e6aDGxLz0dsTQbF5AuCdy9KS7qhWAqS9I8nQAAAAFa5ESRAA')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['5819876497 , 6638578082'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['-1002082869640'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel

# MongoDB information
DATABASE_URI = environ['mongodb+srv://vaqtm:vaqtm@cluster0.a3burak.mongodb.net/?retryWrites=true&w=majority']
DATABASE_NAME = environ['MOVIES']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
default_start_msg = """
**Hi, I'm Media Search bot**

Here you can search files in inline mode. Just press following buttons and start searching.
"""

START_MSG = environ.get('START_MSG', default_start_msg)
SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
INVITE_MSG = environ.get('INVITE_MSG', 'Please join @uzlaynuz to use this bot')
