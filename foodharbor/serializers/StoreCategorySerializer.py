from rest_framework import serializers
from foodharbor.models import StoreCategory

class StoreCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreCategory
        fields = ('id', 'name')