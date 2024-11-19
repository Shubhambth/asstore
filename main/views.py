from django.shortcuts import render , get_object_or_404 , redirect
from .models import Product , PaymentQr
from .forms import PurchaseForm
from django.contrib.auth.decorators import login_required

def index(request):
    product = Product.objects.all() 
    return render(request,'index.html',{'product':product})


def products(request):
    product = Product.objects.all() 
    return render(request,'products.html',{'product':product}) 

@login_required(login_url='/login/')
def product_detail(request,pk):
    product = get_object_or_404(Product,pk=pk)
    return render(request,'product_detail.html',{'product' : product})

@login_required(login_url='/login/')
def purchase_form(request, pk):
    # Get the product the user is trying to purchase
    product = get_object_or_404(Product, pk=pk)
    payment_or = PaymentQr.objects.last()

    if request.method == 'POST':
        form = PurchaseForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            # Save the purchase record with the user and product
            purchase = form.save(commit=False)
            purchase.user = request.user  # Attach the logged-in user to the purchase
            purchase.product = product  # Attach the specific product to the purchase
            purchase.save()  # Save the purchase

            # Redirect to a confirmation page or the product detail page
            return redirect('home')  # Add your success page or other logic here
    else:
        form = PurchaseForm(initial={'product': product})  # Pre-fill the product field

    return render(request, 'purchase_form.html', {'form': form, 'product': product,'payment_or':payment_or})