import asyncio
from aiohttp import ClientSession

from integrations.google_geo_coding import get_geo_code_by_address_async


async def get_geo_location(address, session):
    try:
        geo_data = (await get_geo_code_by_address_async(address, session))
        geo_location = geo_data[0].get('geometry').get('location')
        return {
            'geo_latitude': geo_location.get('lat'),
            'geo_longitude': geo_location.get('lng')
        }
    except Exception:
        pass


async def set_geo_location(row, session):
    row.pop('id', None)
    geo_location = await get_geo_location(row.get('city'), session)
    if geo_location:
        row.update(geo_location)
    return row


async def parse_csv_data(csv_data):
    async with ClientSession() as session:
        tasks = list()
        for row in csv_data:
            tasks.append(set_geo_location(row, session))
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
    return asyncio.run(parse_csv_data(csv_data))
