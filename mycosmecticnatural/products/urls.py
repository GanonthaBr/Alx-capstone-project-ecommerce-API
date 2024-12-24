from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import CategoriesViewSet, ProductsViewSet
from . import views

router = DefaultRouter()
router.register(r'categories',CategoriesViewSet, basename='categories')
router.register(r'products',ProductsViewSet, basename='products')


urlpatterns = [
    path('', include(router.urls)),
    path('wishlist/', views.list_wishlist_products, name='wishlist'),
    path('wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
]