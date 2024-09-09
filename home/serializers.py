from .models import OvozModel
from rest_framework import serializers


class OvozSerializer (serializers.ModelSerializer):
    class Meta:
        model=OvozModel
        fields =['id', 'saylovchi', 'user'] 