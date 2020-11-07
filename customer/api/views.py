from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from customer.api.serializer import CustomerSerializer
from customer.api.models import Customer


class CustomerView(viewsets.ViewSet):
    serializer = CustomerSerializer
    queryset = Customer.objects.all()

    def list(self, request):
        customers_list = self.serializer(data=self.queryset, many=True)
        customers_list.is_valid()
        return Response(customers_list.data)

    def retrieve(self, request, id=None):
        customer = get_object_or_404(self.queryset, id=id)
        customer_serialized = self.serializer(customer)
        return Response(customer_serialized.data)
