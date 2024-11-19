from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('products/',views.products,name='products'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
     path('purchase/<int:pk>/', views.purchase_form, name='purchase'),
]

 