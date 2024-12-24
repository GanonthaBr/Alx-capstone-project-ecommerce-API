from django_filters.rest_framework import  FilterSet, NumberFilter
from .models import Product

class ProductFilter(FilterSet):
    min_price = NumberFilter(field_name="price",lookup_expr='gte')
    max_price = NumberFilter(field_name="price",lookup_expr='lte')
    stock_availability  = NumberFilter(field_name="stock_quantity",lookup_expr='gte')

    class Meta:
        model = Product
        fields = ['min_price', 'max_price', 'stock_availability']