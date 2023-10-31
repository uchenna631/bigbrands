from django.urls import path
from . import views


urlpatterns = [
    path('', views.inventory, name='inventory'),
    path('<int:inventory_id>/', views.product_inventory, name='product_inventory'),
]

