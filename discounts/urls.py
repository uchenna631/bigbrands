from django.urls import path
from . import views

urlpatterns = [
    # list all discounts
    path('', views.discount, name='discount'),

    # Create a new discount for a product with product_id
    path('create/<int:product_id>/', views.create_discount, name='create_discount'),

    # Update a discount with discount_id
    path('update/<int:discount_id>/', views.update_discount, name='update_discount'),

    # Delete a discount with discount_id
    path('delete/<int:discount_id>/', views.delete_discount, name='delete_discount'),
]
