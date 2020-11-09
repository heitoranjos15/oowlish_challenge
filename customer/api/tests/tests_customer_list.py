import json
from random import randrange

from rest_framework import status
from rest_framework.test import APITestCase

from customer.api.tests.helper import CustomerMock


class CustomerPageTests(APITestCase):

    def setUp(self):
        self.mock = CustomerMock()
        self.mock.save_customers_on_db()

    def test_customer_pages(self):
        for page in range(len(self.mock.pages)):
            response = self.client.get(f"/customers/{page + 1}")
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(json.loads(response.content), self.mock.pages[page])

    def test_customer_out_range_page(self):
        response = self.client.get("/customers/800000000")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_invalid_parameter(self):
        response = self.client.get("/customers/asd")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CustomerTests(APITestCase):

    def setUp(self):
        self.mock = CustomerMock()
        self.mock.save_customers_on_db()

    def test_get_customer_by_code(self):
        code = randrange(30)
        response = self.client.get(f"/customer/{code}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), self.mock.list_customer_mock[code - 1])

    def test_invalid_customer_code(self):
        response = self.client.get("/customer/800000000")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_invalid_parameter(self):
        response = self.client.get("/customer/asd")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
