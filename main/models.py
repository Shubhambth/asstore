from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=200)
    image_url = models.URLField(max_length=200 , default='https://ibb.co/NNxVc3V')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='purchases')
    payment_screenshot = models.ImageField(upload_to='tmp/payment_screenshots/')
    name = models.CharField(max_length=100 , default='your name')
    mobile_number = models.CharField(max_length=20 , default='your number')
    email = models.EmailField(default='example@gmail.com')
    purchased_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User : {self.user.username} | Purchased :  {self.product.name}"
    


class PaymentQr(models.Model):
    qr_image = models.URLField(max_length=5000 , default='https://i.postimg.cc/MHHY0gBd/qrcode.jpg')  

    
