from customer.api.models import Customer
from customer.api.builders.pagination import paginate_customers
from customer.api.tests.mocks import customer_mock


class CustomerMock:
    def __init__(self):
        self.list_customer_mock = customer_mock.valid_customer
        self.pages = self.generate_pages()

    def save_customers_on_db(self):
        for customer in self.list_customer_mock:
            mock = Customer(**customer)
            mock.save()

    def generate_pages(self, pages=3):
        list_pages = list()
        for page in range(1, pages + 1):
            list_pages.append(
                paginate_customers(self.list_customer_mock, page))
        return list_pages
