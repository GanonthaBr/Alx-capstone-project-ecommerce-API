from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import CategoriesViewSet

router = DefaultRouter()
router.register(r'categories',CategoriesViewSet, basename='categories')


urlpatterns = [
    path('', include(router.urls)),
]