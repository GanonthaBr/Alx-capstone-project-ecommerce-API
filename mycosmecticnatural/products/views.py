from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from .models import Product, Category, Wishlist, Cart, CartItem
from .serializers import ProductSerializer, CategorySerializer, WishlistSerializer, CartSerializer, CartItemSerializer
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
 


# Cart
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def list_cart_products(request):
    cart = Cart.objects.filter(user=request.user)
    serialized_data = CartSerializer(cart, many=True)
    if not cart:
        return Response({"message":"Your cart is empty!"},status=status.HTTP_404_NOT_FOUND)
    return Response(serialized_data.data, status=status.HTTP_200_OK)

class AddToCart(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, product_id):
        product = Product.objects.get(id=product_id)
        #get or create a Cart for this user       
        cart,created= Cart.objects.get_or_create(user=request.user)
        
        #check if this cart already contains this product
        if CartItem.objects.filter(product=product):
            #get cart item containing this product
            cart_item = CartItem.objects.get(cart=cart,product=product)
            cart_item.delete() #delete it in order to update the quantity
            cart_item = CartItemSerializer(data={"cart":cart.id,"product":product.id, "quantity":cart_item.quantity+1}, partial=True)
            if cart_item.is_valid():
                cart_item.save()
            return Response(cart_item.data,status=status.HTTP_201_CREATED)
        else:
            #add cart item to cart of does not exist
            cart_item = CartItemSerializer(data={"cart":cart.id,"product":product.id, "quantity":1})
            if cart_item.is_valid():
                cart_item.save()
            return Response(cart_item.data,status=status.HTTP_201_CREATED)
    

class RemoveFromCart(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, product_id):
        product = CartItem.objects.get(product=product_id, cart__user=request.user)
        product.delete()
        return Response({"message":"Product removed from cart!"},status=status.HTTP_204_NO_CONTENT)
    
class CartDetails(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        serialized_data = CartItemSerializer(cart_items, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    
class CartUpdate(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self,request,product_id):
        cart = Cart.objects.get(user=request.user)
        product = Product.objects.get(id=product_id)

        cart_item = CartItem.objects.get(cart=cart,product=product)
        quantity = request.query_params.get('quantity')
        cart_item.delete()
        cart_item = CartItemSerializer(data={"quantity":quantity,"cart":cart.id,"product":product.id},partial=True)
        if cart_item.is_valid():
            cart_item.save()
        return Response(cart_item.data,status=status.HTTP_202_ACCEPTED)