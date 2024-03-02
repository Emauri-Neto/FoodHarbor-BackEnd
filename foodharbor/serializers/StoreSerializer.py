from rest_framework import serializers
from foodharbor.models import Store
from foodharbor.serializers import StoreCategorySerializer
from authuser.serializers import PublicUserProfile
from authuser.models import User

class StoreSerializer(serializers.ModelSerializer):
    owner = PublicUserProfile(many=False)
    category = StoreCategorySerializer(many=False)

    class Meta:
        model = Store
        fields = (
            'id',
            'category',
            'fantasy_name',
            'social_reason',
            'owner',
            'description',
            'address',
            'created_at',
        )

class StoreCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = (
            'category',
            'fantasy_name',
            'social_reason',
            'owner',
            'description',
            'address',
        )

    def validate_owner(self, value):
        user = self.context['request'].user

        if user.user_role != 'store':
            raise serializers.ValidationError("Only owners can create a store")
        
        return value

    def create(self, validated_data):
        return Store.objects.create(**validated_data)
