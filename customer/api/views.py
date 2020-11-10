from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework import viewsets
from rest_framework.response import Response

from config import log
from customer.api.serializers import CustomerSerializer
from customer.api.models import Customer
from customer.api.builders.pagination import paginate_customers


class CustomerView(viewsets.ViewSet):
    serializer = CustomerSerializer
    queryset = Customer.objects.all()

    def list(self, request, page=1):
        customers_list = self.serializer(data=self.queryset, many=True)
        customers_list.is_valid()
        page = paginate_customers(customers_list.data, page)
        if not page:
            log.debug(
                {'message': f'Page {page} its out of range',
                    'scope': 'customers/page'}
            )
            return Response({'message': 'Page exceeds the limit'}, status=404)
        return Response(page)

    def retrieve(self, request, id=None):
        try:
            customer = get_object_or_404(self.queryset, id=id)
            customer_serialized = self.serializer(customer)
            return Response(customer_serialized.data)
        except Http404 as error:
            log.debug(
                {'message': f'Customer {id} its not found',
                    'scope': 'customer/id'}
            )
            raise error
