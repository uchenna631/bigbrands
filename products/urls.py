from django.urls import path
from . import views


urlpatterns = [
    # view all products
    path('', views.all_products, name='products'),

    # view product detail
    path('<int:product_id>/', views.product_detail, name='product_detail'),

    # Review a product
    path(
        'reviews/<int:product_id>/', views.product_review,
        name='product_review'),

    # view to add product
    path('add/', views.add_product, name='add_product'),

    # view to edit product
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),

    #  Delete a specific product
    path(
        'delete/<int:product_id>/', views.delete_product,
        name='delete_product'),

    # View all discounts
    path('discounts/', views.discount, name='discounts'),

    # Create a new discount for a product with product_id
    path('create_discount/<int:product_id>/', views.create_discount, name='create_discount'),

    # Update a discount with discount_id
    path('update_discount/<int:discount_id>/', views.update_discount, name='update_discount'),

    # Delete a discount with discount_id
    path('delete_discount/<int:discount_id>/', views.delete_discount, name='delete_discount'),
]
