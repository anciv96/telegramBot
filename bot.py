import asyncio
import logging
import sys

from handlers.send_now_handler import dp
from handlers.cron import interval_sender
from dispatcher import bot, scheduler


async def main() -> None:
    await interval_sender()
    scheduler.start()
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
