from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.models import UserData
from products.models import Product
from .models import Cart, CartItem

# Utility function to get or create user's cart
def get_or_create_user_cart(user):
    cart, created = Cart.objects.get_or_create(user=user)
    return cart

# Add item to cart
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_to_cart(request):
    product_id = request.data.get('product_id')
    quantity = int(request.data.get('quantity', 1))

    try:
        user = request.user
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    cart = get_or_create_user_cart(user)

    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    item.quantity = item.quantity + quantity if not created else quantity
    item.save()

    return Response({'message': 'Product added to cart'}, status=status.HTTP_200_OK)

# View cart items
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def view_cart(request):
    user = request.user

    try:
        cart = Cart.objects.get(user=user)
        items = cart.items.select_related('product').all()

        cart_data = [{
            'product_id': item.product.id,
            'pname': item.product.pname,
            'price': item.product.price,
            'quantity': item.quantity,
            'total': item.quantity * item.product.price
        } for item in items]

        return Response(cart_data, status=status.HTTP_200_OK)

    except Cart.DoesNotExist:
        return Response([], status=status.HTTP_200_OK)

# Remove item from cart
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def remove_item_from_cart(request):
    product_id = request.data.get('product_id')

    try:
        user = request.user
        cart = Cart.objects.get(user=user)
        item = CartItem.objects.get(cart=cart, product_id=product_id)
        item.delete()
        return Response({'message': 'Item removed from cart'}, status=status.HTTP_200_OK)
    except (Cart.DoesNotExist, CartItem.DoesNotExist):
        return Response({'error': 'Item not found in cart'}, status=status.HTTP_404_NOT_FOUND)

# Checkout cart
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def checkout_cart(request):
    try:
        user = request.user
        cart = Cart.objects.get(user=user)
        items = cart.items.select_related('product').all()

        if not items:
            return Response({'message': 'Cart is already empty'}, status=status.HTTP_200_OK)

        total_amount = sum(item.quantity * item.product.price for item in items)

        # Here you can also generate an Order model instance and save order details

        items.delete()  # Clear cart after checkout
        return Response({'message': 'Checkout successful', 'total': total_amount}, status=status.HTTP_200_OK)

    except Cart.DoesNotExist:
        return Response({'message': 'Cart is empty'}, status=status.HTTP_200_OK)
