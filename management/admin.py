from django.contrib import admin
from checkout.models import OrderManager


@admin.register(OrderManager)
class OrderManagerAdmin(admin.ModelAdmin):
    readonly_fields = ('order',)
    
    list_display = (
        'order', 'processed', 'processed_by',
        'processed_date', 'delivered', 'delivered_by',
        'delivered_date', 'status')
