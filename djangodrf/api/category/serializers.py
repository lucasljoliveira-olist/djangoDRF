from rest_framework import serializers
from .models import Category, BannedCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BannedCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BannedCategory
        fields = '__all__'
