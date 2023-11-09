from django.shortcuts import render
from .models import Product     # Can use .models as it is in the same directory / application as this file

# Create your views here.

def product_list(request):
    products = Product.objects.all().order_by('-date_added')     # Returns all objects with Product and orders them by date added, with the oldest results showing first
    return render(request, 'product/product_list.html', {'products': products})
