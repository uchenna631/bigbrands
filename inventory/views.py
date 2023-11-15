from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Inventory
from .forms import InventoryForm


@login_required
def inventory(request):
    """ A view to show all products, including sorting and search queries """

     # Redirect unauthorised users to the home page
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    inventories = Inventory.objects.all()
    context = {
        'inventories': inventories
    }
    return render(request, 'inventory/inventory.html', context)


@login_required
def product_inventory(request, inventory_id):
    '''A view to show the inventory of a particular product.
     The product inventory could be updated as well'''

    # Redirect unauthorised users to the home page
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    inventory = get_object_or_404(Inventory, pk=inventory_id)
    inventories = Inventory.objects.all()

    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=inventory)
        if form.is_valid():
            form.save()
            return redirect('inventory')
    else:
        form = InventoryForm(instance=inventory)
    context =  {'inventory': inventory, 'form': form}
    return render(request, 'inventory/product_inventory.html', context)
