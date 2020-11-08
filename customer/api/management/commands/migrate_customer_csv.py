import csv
from django.core.management.base import BaseCommand, CommandError

from customer.api.serializers import CustomerSerializer
from customer.api.builders.customer import build_customer


class Command(BaseCommand):
    help = 'Add customers from a csv file to the database'

    def add_arguments(self, parser):
        parser.add_argument('--path',
                            type=str,
                            help='Inform complete csv location path')

    def save_customer_from_csv(self, path):
        with open(path) as csv_file:
            csv_rows = csv.DictReader(csv_file, delimiter=',')
            list_customer = build_customer(csv_rows)

            for cont, customer in enumerate(list_customer):
                customer_serialized = CustomerSerializer(data=customer)
                if customer_serialized.is_valid():
                    customer_serialized.save(customer)
                else:
                    self.stdout.write(
                        f'Row {cont + 2} is not valid, please check if this row is valid')

    def handle(self, *args, **kwargs):
        path = kwargs["path"]
        if path.endswith('.csv'):
            try:
                self.save_customer_from_csv(path)
            except Exception:
                raise CommandError(
                    f'Check if the path: {path} is correct, or the data on csv is correct')
        else:
            raise CommandError('File path parameter is invalid')
