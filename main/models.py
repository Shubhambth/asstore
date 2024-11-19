from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='product_image/',default='logo.png')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='purchases')
    payment_screenshot = models.ImageField(upload_to='payment_screenshots/')
    email = models.EmailField(default='example@gmail.com')
    purchased_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User : {self.user.username} | Purchased :  {self.product.name}"
    


class PaymentQr(models.Model):
    qr_image = models.ImageField(upload_to='qrimage/')

    