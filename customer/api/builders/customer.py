from aiohttp import ClientSession
import asyncio

from customer.api.builders.geo_location import get_geo_location 


async def __set_geo_location(row, session):
    geo_location = await get_geo_location(row.get('city'), session)
    if geo_location:
        row.update({'geo_location': geo_location})
        return row


async def __parse_csv_data(csv_data):
    async with ClientSession() as session:
        tasks = list()
        for row in csv_data:
            row.pop('id', None)
            tasks.append(__set_geo_location(row, session))
        return await asyncio.gather(*tasks)


def build_customer(csv_data):
    """
    Description
    ----------
    Build Customer Object from csv data

    Parameters
    ----------
    csv_data : csv
        csv rows

    Returns
    -------
    list
        Dict with all customer data
    """
    return asyncio.run(__parse_csv_data(csv_data))
