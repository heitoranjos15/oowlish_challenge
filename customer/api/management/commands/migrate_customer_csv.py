import csv
from django.core.management.base import BaseCommand, CommandError
from customer.api.serializer import CustomerSerializer
from customer.settings import BASE_DIR


class Command(BaseCommand):
    help = 'Add customers from a csv file to the database'

    def add_arguments(self, parser):
        parser.add_argument('--path',
                            type=str,
                            help='Inform complete csv location path')

    def save_customer_from_csv(self, path):
        with open(path) as csv_file:
            csv_rows = csv.DictReader(csv_file, delimiter=',')
            for cont, row in enumerate(csv_rows):
                row.pop('id', None)
                customer = CustomerSerializer(data=row)
                if customer.is_valid():
                    customer.save(row)
                else:
                    self.stdout.write(f'Row {cont} is not valid, failed to insert')

    def handle(self, *args, **kwargs):
        path = f'{BASE_DIR}/{kwargs["path"]}'
        if path.endswith('.csv'):
            try:
                self.save_customer_from_csv(path)
            except Exception:
                raise CommandError(
                    f'Check if the path: {path} is correct, or the data on csv is correct')
        else:
            raise CommandError('File path parameter is invalid')
