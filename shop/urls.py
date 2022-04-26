from django.contrib import admin
from django.urls import path
from . import views
app_name = 'shop'


urlpatterns = [
    path('', views.get_product_list, name='product_list'),
    path('add-product/', views.create_product, name='add_product'),
    path('delete/<str:product_slug>/', views.delete_product, name='delete_product'),
    path('<str:category_slug>/', views.get_product_list, name='product_list_by_category'),
    path('products/<str:product_slug>/', views.get_product_detail, name='product_detail'),
]




