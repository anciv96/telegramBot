
import aiofiles
import logging
from services.scraper import Scraper
from config import LOCAL_FEED_FILE_PATH, ARTICLES_HISTORY_FILE_PATH


class Database(Scraper):
    async def _read_data_from_local_file(self) -> str:
        async with aiofiles.open(LOCAL_FEED_FILE_PATH, 'r') as file:
            data = await file.read()
            return data

    async def rewrite_data_in_local_file(self):
        logging.info('Rewroten')
        async with aiofiles.open(LOCAL_FEED_FILE_PATH, 'w') as file:
            data = await self.get_data_from_feed()
            await file.write(data)

    async def _add_new_article_to_history_file(self, article_id):
        async with aiofiles.open(ARTICLES_HISTORY_FILE_PATH, 'a') as file:
            await file.writelines(article_id + '\n')

    async def _read_items_from_history(self):
        async with aiofiles.open(ARTICLES_HISTORY_FILE_PATH, 'r') as file:
            src = (await file.read()).split('\n')
            return src
