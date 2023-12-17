import asyncio
from contextlib import suppress

from bs4 import BeautifulSoup

from services.database.database import Database
from config import hideList


class ConvertLocalFileToBs4Objects(Database):
    async def __get_all_offers(self):
        data = await self._read_data_from_local_file()
        soup = BeautifulSoup(data, "xml")
        try:
            offers = soup.find('yml_catalog').find('shop').find('offers').find_all('offer')
            return offers
        except AttributeError:
            await asyncio.sleep(5)
            return await self.__get_all_offers()

    async def _get_parameters_list_from_config(self) -> list:
        """Получает список параметров из конфига, которые должны быть в тексте сообщения"""
        params_list = hideList
        params_list_cleaned = [x.strip() for x in params_list.split(',')]
        return params_list_cleaned

    async def _get_messages(self, messages_quantity: int) -> list:
        items_from_local_file = await self.__get_all_offers()
        items = []

        for item in items_from_local_file:
            if len(items) < messages_quantity:
                item_url = item.find('vendorCode').text

                if item_url in (await self._read_items_from_history()):
                    continue

                await self._add_new_article_to_history_file(item_url)
                items.append(item)

        return items


class ConvertObjectsToDict:

    async def __convert_constant_parameters(self, item) -> dict:
        data = {
            'name': item.find('name').text,
            'img': item.find('picture').text,
            'url': item.find('url').text
        }
        with suppress(AttributeError):
            price = item.find('price').text
            data['price'] = price
        with suppress(AttributeError):
            currency = item.find('currencyId').text
            data['currency'] = currency

        return data

    async def __convert_variable_parameters(self, parameters: list, item):
        data = {
            'params': {}
        }

        for parameter in parameters:
            with suppress(AttributeError):
                param_value = item.find('param', {'name': parameter}).text
                data['params'][parameter] = param_value

        return data

    async def _convert_all_data(self, item, parameters):
        required_data = await self.__convert_constant_parameters(item)
        optional_data = await self.__convert_variable_parameters(parameters, item)

        return required_data | optional_data


class Converter(ConvertLocalFileToBs4Objects, ConvertObjectsToDict,):
    async def get_message_data(self, messages_quantity: int) -> list:
        """returns messages list"""
        items = await self._get_messages(messages_quantity)
        item_parameters = await self._get_parameters_list_from_config()

        data = []

        for item in items:
            data.append(await self._convert_all_data(item, item_parameters))

        return data
