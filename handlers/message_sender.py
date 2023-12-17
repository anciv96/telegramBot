from dispatcher import bot
from config import extra_text, CHANNELS_ID
from services.xml_converter import Converter

converter = Converter()


async def _make_message_text(data: dict) -> str:
    """Составляет текст сообщения используя данныe из спарсенных данных"""
    price = '{0:,}'.format(int(float(data['price']))).replace(',', ' ')
    message_text = f"*{data['name']}*\n\n"

    for k, v in data['params'].items():
        message_text += f'• {k}: {v}\n'

    message_text += f"• цена: {price} {data['currency']}\n"

    message_text += '\n' + extra_text + '\n\n'
    message_text += data['url']

    return message_text


async def _send_item_messages(messages: list):

    for message in messages:
        message_text = await _make_message_text(message)
        for channel in CHANNELS_ID:
            await bot.send_photo(
                channel,
                photo=message['img'],
                caption=str(message_text),
                parse_mode='MARKDOWN'
            )


async def get_messages_and_send(messages_quantity: int) -> None:
    await converter.rewrite_data_in_local_file()
    messages = await converter.get_message_data(messages_quantity)
    await _send_item_messages(messages)

