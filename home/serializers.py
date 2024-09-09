from rest_framework import serializers
from .models import OvozModel

class OvozSerializer(serializers.ModelSerializer):
    class Meta:
        model = OvozModel
        fields = ['id', 'user']
