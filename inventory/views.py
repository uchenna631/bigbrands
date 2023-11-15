from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .models import Inventory
from .forms import InventoryForm


def inventory(request):
    """ A view to show all products, including sorting and search queries """

    inventories = Inventory.objects.all()
    context = {
        'inventories': inventories
    }
    return render(request, 'inventory/inventory.html', context)


def product_inventory(request, inventory_id):
    '''A view to show the inventory of a particular product.
     The product inventory could be updated as well'''
     
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
