from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/cart/', views.store, name='store'),
    path('product/', views.product_list, name='product_list'),      # This is from a view called product_list!
    path('product/<slug:category_slug>/', views.category_products, name='category_products'),     # This is from a view called category_products!
    path('product/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),  # This is from a view called product_detail!
    
]