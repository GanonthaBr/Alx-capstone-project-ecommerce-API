from rest_framework import serializers
from .models import Product, Category, Wishlist, Cart, CartItem

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


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'

    def validate(self, attrs):
        if Wishlist.objects.filter(user=attrs.get('user'), product=attrs.get('product')).exists():
            raise serializers.ValidationError('Product is already in wishlist')
        return super().validate(attrs)
    

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
    # if product exists, increase quantity

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product','quantity','cart']