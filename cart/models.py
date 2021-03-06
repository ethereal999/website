from django.db import models
from django.contrib.auth.models import User
from blog.models import Product, Variation


class CartItem(models.Model):
    cart = models.ForeignKey('Cart', related_name="cart_item", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="product", on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation, blank=True)
    quantity = models.IntegerField(default=1)
    line_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.product.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart_user")
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    qty = models.IntegerField(default=1)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)