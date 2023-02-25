from rest_framework import serializers

from test_endpoint.function_handler.models import *


class ASerializer(serializers.ModelSerializer):
    class Meta:
        model = A
        fields = ('value', 'color')


class BSerializer(serializers.ModelSerializer):
    class Meta:
        model = B
        fields = ('function', 'value')

class CSerializer(serializers.ModelSerializer):
    class Meta:
        model = C
        fields = ('value')
