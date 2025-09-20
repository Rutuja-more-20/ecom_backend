# cart/models.py
from django.db import models
from users.models import UserData
from products.models import Product

class Cart(models.Model):
    user = models.ForeignKey(UserData, on_delete=models.CASCADE, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('cart', 'product')
