from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from .models import Product, Category, Wishlist
from .serializers import ProductSerializer, CategorySerializer, WishlistSerializer
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import PostPagination
from .filters import ProductFilter
# Create your views here.
class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request):
        serialized_data = CategorySerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['name__icontains', 'category__name__icontains']
    pagination_class = PostPagination
    filterset_class = ProductFilter

    def post(self, request):
        serialized_data = ProductSerializer(data = request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def list_wishlist_products(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    serialized_data = WishlistSerializer(wishlist, many=True)
    if not wishlist:
        return Response({"message":"Your wish list is empty!"},status=status.HTTP_404_NOT_FOUND)
    return Response(serialized_data.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_to_wishlist(request, product_id):
    product = Product.objects.get(id=product_id)
    serialized_data = WishlistSerializer(data={'product':product.id, 'user':request.user.id})
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def remove_from_wishlist(request, product_id):
    product = Wishlist.objects.get(product=product_id, user=request.user)
    product.delete()
    return Response({"message":"Product removed from wish list!"},status=status.HTTP_204_NO_CONTENT)
 