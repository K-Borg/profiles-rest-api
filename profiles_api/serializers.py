#For post and put API functionality available in view, this receives content
# posted to api and validates it (correct type)- it's like a form.
from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)
