import calendar
from datetime import datetime, date

from apscheduler.triggers.cron import CronTrigger

from handlers.message_sender import get_messages_and_send
from dispatcher import scheduler, moscow_tz
from config import working_days, DAYS_CONVERTER, work_end_time, work_start_time, interval_time, messages_quantity


async def _convert_days_from_config() -> str:
    if '*' in working_days:
        return '*'

    days = [x.strip() for x in working_days.split(',')]
    converted_days = ','.join([DAYS_CONVERTER[x] for x in days])

    return converted_days


async def make_exact_date_from_interval_time(moment) -> str:
    if moment == 0:
        work_time = work_start_time.strip().split(':')
    else:
        work_time = work_end_time.strip().split(':')

    today_date = datetime.now().date()

    work_hour = work_time[0]
    work_minute = work_time[1]
    start_date = f'{today_date} {work_hour}:{work_minute}:00'

    return start_date


async def schedule_handler():
    messages = 15 if int(messages_quantity) > 15 else int(messages_quantity)
    await get_messages_and_send(messages)


async def interval_sender():
    days = await _convert_days_from_config()

    today_date = date.today()
    week_day = calendar.day_name[today_date.weekday()]
    week_day_short = week_day[:3].lower()

    if week_day_short in days.split(',') or '*' in days.split(','):
        print('start')

        start_date = await make_exact_date_from_interval_time(0)
        end_date = await make_exact_date_from_interval_time(1)

        scheduler.add_job(schedule_handler,
                          'interval',
                          seconds=int(interval_time),
                          start_date=start_date,
                          end_date=end_date,
                          timezone=moscow_tz
                          )


async def cron():

    trigger = CronTrigger(
        day_of_week='*',
        hour=00,
        minute=1,
        timezone=moscow_tz
    )

    scheduler.add_job(interval_sender,
                      trigger=trigger,
                      max_instances=1,
                      )
