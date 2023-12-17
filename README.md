# AutoEuropaRepostBot

Telegram bot, that scrapes information from api, converts it, and sends to channels in definite interval. Admins can send messages, without waiting the time, by clicking /send_now button, in settings (See below).

Bot was written in python3.10, in async library aiogram==3.2.0.

## Installation

Clone repository
```bash
git clone https://github.com/anciv96/telegramBot.git
```

Create and activate environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

To install all libraries, run:
```bash
pip install -r requirements.txt
```

## Usage
In base directory, bot can be edited in file config.ini. It looks like this:

```ini
[DEFAULT]
bot_token = XXXXX:1234567
channels_id = -10012345678, -1009876543
admins = all

[MESSAGE]
; URL
URL = https://link_to_xml_api


; how many items to place at a time
messages_quantity_per_time = 5

; items placement speed (in minutes)
message_send_interval = 65

; working hours (in this case from 9 am to 6 pm)
work_start_time = 09:00
work_end_time = 18:00

; working days (on which days to post)
; воскресенье
; понедельник
; вторник
; среда
; четверг
; пятница
; суббота
; all days: *
working_days = *

; list of fields to place
hideList=привод, топливо,объём, цвет

; custom text at the top of the URL
text = Срочно!

# For developers
Bot is fully asynchronous, so do not use sync libraries. As cron library, was chosen APScheduler (AsyncIOScheduler mode).

Id's of sent advertisements are saved in the service/urls_history.txt. And each time, the bot checks whether there is a record in the file, if not, then items are new.
