from rest_framework import serializers
from customer.api.models import Customer


class CustomerSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=45)
    last_name = serializers.CharField(max_length=30, allow_blank=True)
    email = serializers.RegexField(
        regex=r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
    gender = serializers.CharField(min_length=4, max_length=6)
    company = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)
    title = serializers.CharField(max_length=100, allow_blank=True)
    geo_latitude = serializers.FloatField()
    geo_longitude = serializers.FloatField()

    def save(self, validate_data):
        customer = Customer(**validate_data)
        customer.save()
        return customer

    def save_customer_list(self, validate_list):
        Customer.objects.bulk_create(validate_list)
