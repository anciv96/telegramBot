from aiogram.filters import Command
from dispatcher import dp
from handlers.message_sender import get_messages_and_send


@dp.message(Command('send_now'))
async def command_start_handler() -> None:
    await get_messages_and_send(1)
