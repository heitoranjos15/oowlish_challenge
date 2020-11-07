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
    geo_latitude = serializers.FloatField(allow_null=True, required=False)
    geo_longitude = serializers.FloatField(allow_null=True, required=False)

    def save(self, validate_date):
        customer = Customer(**validate_date)
        customer.save()
        return customer
