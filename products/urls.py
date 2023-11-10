from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path(
        'reviews/<int:product_id>/', views.product_review,
        name='product_review'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path(
        'delete/<int:product_id>/', views.delete_product,
        name='delete_product'),

    path('discounts/', views.discount, name='discounts'),

    # Create a new discount for a product with product_id
    path('create_discount/<int:product_id>/', views.create_discount, name='create_discount'),

    # Update a discount with discount_id
    path('update_discount/<int:discount_id>/', views.update_discount, name='update_discount'),

    # Delete a discount with discount_id
    path('delete_discount/<int:discount_id>/', views.delete_discount, name='delete_discount'),
]
