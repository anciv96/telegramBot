import aiohttp
from config import URL, HEADERS


class Scraper:
    """Парсит xml информацию с сайта донара"""

    @staticmethod
    async def get_data_from_feed():
        async with aiohttp.ClientSession(headers=HEADERS, trust_env=True) as session:
            async with session.get(URL, ssl=False) as resp:
                request = await resp.text()
                data = request.replace('\t', ' ' * 4)
                return data
