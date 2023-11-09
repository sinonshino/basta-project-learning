from django.shortcuts import render, get_object_or_404
from .models import Product     # Can use .models as it is in the same directory / application as this file

# Create your views here.

def product_list(request):
    products = Product.objects.all().order_by('-date_added')     # Returns all objects with Product and orders them by date added, with the oldest results showing first
    return render(request, 'product/product_list.html', {'products': products})     # product/product_list.html is the template that displays

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product/product_detail.html', {'product': product})     # product/product_detail.html is the template that displays
