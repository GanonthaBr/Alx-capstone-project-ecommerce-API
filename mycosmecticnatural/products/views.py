from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework import viewsets
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
    