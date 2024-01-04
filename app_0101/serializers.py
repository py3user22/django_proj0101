from rest_framework import serializers
from .models import MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        # must match the model fields
        fields = ['id',
                  'title',
                  'price',
                  'inventory']
