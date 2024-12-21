from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

# Create your views here.
class CategoryView(APIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        items = Category.objects.all()
        serializered_data = CategorySerializer(items, many=True)
        return Response(serializered_data.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serialized_item = CategorySerializer(data=request.data, context={'request': request})
        if serialized_item.is_valid():
            serialized_item.save()
            return Response(serialized_item.data, status=status.HTTP_201_CREATED)
        return Response(serialized_item.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            item = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
        serialized_item = CategorySerializer(item, data=request.data, context={'request': request},partial=True)
        if serialized_item.is_valid():
            serialized_item.save()
            return Response(serialized_item.data, status=status.HTTP_200_OK)
        return Response(serialized_item.errors, status=status.HTTP_400_BAD_REQUEST)