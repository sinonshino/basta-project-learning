from django.contrib import admin
from .models import Product     # Include the Product Model

# Register the Product Model
admin.site.register(Product)