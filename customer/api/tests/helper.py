from customer.api.serializers import GeoLocationSerializer, CustomerSerializer
from customer.api.builders.pagination import paginate_customers
from customer.api.tests.mocks import customer_mock


class CustomerMock:
    def __init__(self):
        self.list_customer_mock = customer_mock.valid_customer
        self.pages = list()

    def save_customers_on_db(self):
        geo_location_data = {
            'address': 'Defaul Local',
            'geo_latitude': 39.724953,
            'geo_longitude': -52.806863
        }
        geo_location_serializer = GeoLocationSerializer(data=geo_location_data)
        geo_location_serializer.is_valid()
        geo_location = geo_location_serializer.save(geo_location_data)

        for customer in self.list_customer_mock:
            mock = CustomerSerializer(data=customer)
            if mock.is_valid():
                mock.save({
                    "first_name": customer.get('first_name'),
                    "last_name": customer.get('last_name'),
                    "email": customer.get('email'),
                    "gender": customer.get('gender'),
                    "company": customer.get('company'),
                    "city": customer.get('city'),
                    "title": customer.get('title'),
                    'geo_location': geo_location
                })

    def set_pages(self, pages=3):
        for page in range(1, pages + 1):
            self.pages.append(
                paginate_customers(self.list_customer_mock, page))
