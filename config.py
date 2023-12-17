import configparser


config = configparser.ConfigParser()
config.read('config.ini')

TOKEN = config.get('DEFAULT', 'bot_token')
CHANNELS_ID = config.get('DEFAULT', 'channels_id')

URL = config.get('MESSAGE', 'URL')
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
              '*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
}

# Time Settings
working_days = config.get('MESSAGE', 'working_days')
DAYS_CONVERTER = {
    'воскресенье': 'sun',
    'понедельник': 'mon',
    'вторник': 'tue',
    'среда': 'wed',
    'четверг': 'thu',
    'пятница': 'fri',
    'суббота': 'sat',
}
interval_time = config.get('MESSAGE', 'message_send_interval')
work_start_time = config.get('MESSAGE', 'work_start_time')
work_end_time = config.get('MESSAGE', 'work_end_time')

# Message text
extra_text = config.get('MESSAGE', 'text')
hideList = config.get('MESSAGE', 'hideList')
messages_quantity = config.get('MESSAGE', 'messages_quantity_per_time')

# Database
LOCAL_FEED_FILE_PATH = 'services/database/data.yml'
ARTICLES_HISTORY_FILE_PATH = 'services/database/urls_history.txt'
