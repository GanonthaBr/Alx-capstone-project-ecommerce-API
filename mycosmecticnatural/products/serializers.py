from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate(self, attrs):
        if attrs.get('price') <= 0:
            raise serializers.ValidationError('Price must be greater than 0')
        return super().validate(attrs)
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'