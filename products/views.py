from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Review, Discount
from .forms import ProductForm, ReviewForm, DiscountForm
from checkout.models import Order, OrderLineItem


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                msg = "You didn't enter any search criteria!"
                messages.error(request, msg)
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            msg = 'Failed to add product. Please ensure the form is valid.'
            messages.error(request, msg)
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            msg = 'Failed to update product. Please ensure the form is valid.'
            messages.error(request, msg)
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def product_review(request, product_id):
    ''' A view to review products  '''
    
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, 'Successfully added a review!')
            return redirect(reverse('product_review', args=[product.id]))
        else:
            msg = 'Product review failed. Please ensure the form is valid.'
            messages.error(request, msg)
    else:
        form = ReviewForm()
        context = {'product': product, 'reviews': reviews, 'form': form}
        return render(
            request, 'products/product_review.html', context)


@login_required
def discount(request):
    ''' List all discounts '''
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can access this page.')
        return redirect(reverse('home'))
    discounts = Discount.objects.all()
    return render(request, 'products/discounts.html', {'discounts': discounts})


@login_required
def create_discount(request, product_id):
    '''  Create a new discount for a product with product_id '''
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id) 
    if request.method == 'POST':
        form = DiscountForm(request.POST)
        if form.is_valid():
            discount = form.save(commit=False)
            discount.product = product
            discount.save()
            messages.success(request, 'Product discount created successfully!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            msg = 'Product discount creation failed. Please ensure the form is valid.'
            messages.error(request, msg)
    else:
        form = DiscountForm(initial={'product': product})
    context = {'form': form, 'product': product }
    return render(request, 'products/create_discount.html', context)


@login_required
def update_discount(request, discount_id):
    ''' Update a discount with discount_id '''
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    discount = get_object_or_404(Discount, pk=discount_id)
    if request.method == 'POST':
        form = DiscountForm(request.POST, instance=discount)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product discount created successfully!')
            return redirect('discounts')
        else:
            messages.error(request, 'Product discount creation failed!')
    else:
        form = DiscountForm(instance=discount)
    return render(request, 'products/update_discount.html', {'form': form, 'discount': discount})


@login_required
def delete_discount(request, discount_id):
    '''  Delete a discount with discount_id '''
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    discount = get_object_or_404(Discount, pk=discount_id)
    if request.method == 'POST':
        discount.delete()
        messages.success(request, 'Product discount deleted successfully!')
        return redirect('discounts')
    return render(request, 'products/delete_discount.html', {'discount': discount})
