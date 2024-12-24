from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import CategoriesViewSet, ProductsViewSet

router = DefaultRouter()
router.register(r'categories',CategoriesViewSet, basename='categories')
router.register(r'products',ProductsViewSet, basename='products')


urlpatterns = [
    path('', include(router.urls)),
]