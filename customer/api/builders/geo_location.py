from config import log
import json


from customer.api.models import GeoLocation
from customer.api.serializers import GeoLocationSerializer

from integrations.google_geo_coding import get_geo_code_by_address_async

scope = json.dumps({'scope': 'command/geo_location'})


async def __save_geo_location(geo_data, address):
    serializer = GeoLocationSerializer({
        'geo_latitude': geo_data.get('lat'),
        'geo_longitude': geo_data.get('lng'),
        'address': address
    })
    if serializer.is_valid():
        return serializer.save()
    raise Exception(f'Geo Location API return its not valid: {geo_data}')


async def get_geo_location(address, session):
    try:
        geo_location = GeoLocation.objects.filter(address=address).first()
        if not geo_location:
            google_response = await get_geo_code_by_address_async(address, session)
            geo_data = google_response[0].get('geometry').get('location')
            geo_location = __save_geo_location(geo_data, address)
        return geo_location
    except Exception as error:
        log.debug('Error to get geo_location_data', error.__str__(), scope)
