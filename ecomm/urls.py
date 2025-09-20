"""
URL configuration for ecomm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from cart.views import add_to_cart, checkout_cart, remove_item_from_cart, view_cart
from orders.views import cancel_order, cancelOrder, checkout_carts, createOrder, get_all_orders, get_user_orders, getAllOrders, getUserOrders, update_order_status, updateOrderStatus
from products.views import addProduct, deleteProduct, getAllProducts, getProduct, updateProduct
from users.views import deleteUser, getAllUsers, getUser, login_view, loginUser, logoutUser, registeruser, updateUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('getAllUsers/',getAllUsers),
    path('logoutUser/',logoutUser),
    path('getUser/<str:username>',getUser),
    path('registeruser/',registeruser),
    path('deleteUser/<str:userfromclient>',deleteUser),
    path('updateUser/',updateUser),
    path('loginUser/',loginUser),
    path('getAllProducts/',getAllProducts),
    path('getProduct/<str:pname>',getProduct),
    path('deleteProduct/<str:pname>',deleteProduct),
    path('addProduct/',addProduct),
    path('updateProduct/',updateProduct),
    path('getAllOrders/<str:username>',getAllOrders),
    path('createOrder/',createOrder),
    path('getUserOrders/',getUserOrders),
    path('updateOrderStatus/',updateOrderStatus),  
    path('cancelOrder/',cancelOrder),
    path('add_to_cart/',add_to_cart),
    path('view_cart/<str:username>',view_cart),
    path('remove_item_from_cart/', remove_item_from_cart),
    path('checkout_cart/',checkout_cart),
    path('login_view/',login_view),
    path('cancel_order/',cancel_order),
    path('update_order_status/',update_order_status),
    path('get_all_orders/',get_all_orders),
    path('get_user_orders/',get_user_orders),
    path('checkout_carts/',checkout_carts)

]
