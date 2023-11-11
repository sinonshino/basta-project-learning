from django.shortcuts import render, get_object_or_404
from .models import Product, Category     # Can use .models as it is in the same directory / application as this file

# Create your views here.

def home(request):
    categories = Category.objects.filter(parent__isnull=True)     # This needs to be passed into any and every view that has the extends base.html
    subcategories = Category.objects.filter(parent__isnull=False) # As well as this line
    return render(request, 'product/home.html', {'categories': categories, 'subcategories': subcategories})

def product_list(request):
    products = Product.objects.all().order_by('-date_added')     # Returns all objects with Product and orders them by date added, with the oldest results showing first
    return render(request, 'product/product_list.html', {'products': products})     # product/product_list.html is the template that displays

def product_detail(request, category_slug, product_slug):
    categories = Category.objects.filter(parent__isnull=True)     # This needs to be passed into any and every view that has the extends base.html
    subcategories = Category.objects.filter(parent__isnull=False) # As well as this line
    product = get_object_or_404(Product, slug=product_slug)
    category = get_object_or_404(Category, slug=category_slug)
    return render(request, 'product/product_detail.html', {'product': product, 'category': category, 'categories': categories, 'subcategories': subcategories})

def category_products(request, category_slug):
    categories = Category.objects.filter(parent__isnull=True)     # This needs to be passed into any and every view that has the extends base.html
    subcategories = Category.objects.filter(parent__isnull=False) # As well as this line
    category = get_object_or_404(Category, slug=category_slug)     # Get the category's slug
    products = category.products.all()    # Filter to only get objects that are related to that catergories' slug
    return render(request, 'product/category_products.html', {'category': category, 'products': products, 'categories': categories, 'subcategories': subcategories})

def store(request):
    return render(request, 'product/cart.html')

def base(request):
    categories = Category.objects.all()
    return render(request, 'product/base.html', {'categories': categories})     # product/category_list.html is the template that displays