import time
from config import enviroment


async def get_geo_code_by_address_async(address, session):
    """
    Description
    ----------
    Geo Code API integration

    Parameters
    ----------
    address : str
        Address to search on google
    session : ClientSession
        Session object

    Returns
    -------
    list
        Geo Location result
    """

    params = {
        'key': enviroment.google_api_key,
        'address': address
    }
    request = await session.request(
        'GET', enviroment.google_host, params=params)
    response = await request.json()
    geo_location = response.get('results')

    if not geo_location:
        error_message = response.get('status')
        if error_message == 'OVER_QUERY_LIMIT':
            # If Google returns OVER_QUERY_LIMIT give a 0.2 seconds break and retry again
            time.sleep(0.2)
            return await get_geo_code_by_address_async(address, session) # retry
        else:
            raise Exception(error_message)

    return geo_location
