import csv
from django.core.management.base import BaseCommand, CommandError
from customer.api.models import Customer
from customer.settings import BASE_DIR


class Command(BaseCommand):
    help = 'Add customers from a csv file to the database'

    def add_arguments(self, parser):
        parser.add_argument('--path',
                            type=str,
                            help='Inform complete csv location path')

    def get_customers(self, path):
        customer_list = list()
        with open(path) as csv_file:
            csv_rows = csv.DictReader(csv_file, delimiter=',')
            for row in csv_rows:
                row.pop('id', None)
                customer = Customer(**row)
                customer_list.append(customer)
        return customer_list

    def handle(self, *args, **kwargs):
        path = f'{BASE_DIR}/{kwargs["path"]}'
        if path.endswith('.csv'):
            try:
                customer_list = self.get_customers(path)
                Customer.objects.bulk_create(customer_list)
            except Exception as exception:
                self.stdout.write(f'asdd {exception}')
                raise CommandError(
                    f'Check if the path: {path} is correct, or the data on csv is correct')
        else:
            raise CommandError('File path parameter is invalid')
