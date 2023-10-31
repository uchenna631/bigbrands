from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .models import Discount
from .forms import DiscountForm


# List all discounts
def discount(request):
    discounts = Discount.objects.all()
    return render(request, 'discounts/discounts.html', {'discounts': discounts})

# Create a new discount for a product with product_id
def create_discount(request, product_id):
    product = get_object_or_404(Product, pk=product_id)  # Assuming you have a Product model
    if request.method == 'POST':
        form = DiscountForm(request.POST)
        if form.is_valid():
            discount = form.save(commit=False)
            discount.product = product
            discount.save()
            return redirect('discounts')
    else:
        form = DiscountForm()
    return render(request, 'discounts/create_discount.html', {'form': form})

# Update a discount with discount_id
def update_discount(request, discount_id):
    discount = get_object_or_404(Discount, pk=discount_id)
    if request.method == 'POST':
        form = DiscountForm(request.POST, instance=discount)
        if form.is_valid():
            form.save()
            return redirect('discounts')
    else:
        form = DiscountForm(instance=discount)
    return render(request, 'discounts/update_discount.html', {'form': form, 'discount': discount})

# Delete a discount with discount_id
def delete_discount(request, discount_id):
    discount = get_object_or_404(Discount, pk=discount_id)
    if request.method == 'POST':
        discount.delete()
        return redirect('discounts')
    return render(request, 'discounts/delete_discount.html', {'discount': discount})

# def discounts(request):
#     """ A view to show all products, including sorting and search queries """

#     discounts = Discount.objects.all()
#     context = {
#         'discounts': discounts
#     }
#     return render(request, 'discounts/discounts.html', context)


# def product_discount(request, product_id):
#     product = Product.objects.get(pk=product_id)
#     discount = Discount.objects.get(product=product)

#     if request.method == 'POST':
#         form = DiscountForm(request.POST, instance=product)
#         if form.is_valid():
#             form.save()
#             return redirect('product.product_detail', product_id=product.id)
#     else:
#         form = DiscountForm(instance=discount)

#     return render(request, 'discounts/product_discount.html', {'product': product, 'form': form})
