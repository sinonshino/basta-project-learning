from django.contrib import admin
from .models import Product, Category     # Include the Product and Category Models

# Register the Product Model
admin.site.register(Product)
# Register the Category Model
admin.site.register(Category)