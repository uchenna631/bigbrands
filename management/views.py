from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from checkout.models import OrderManager


@login_required
def order_manager(request):
    if not request.user.is_superuser:
        messages.error('Only a store owner can access this page')
    orders = get_object_or_404(OrderManager)
    return render(request, 'management/management.html', {'orders': orders})
