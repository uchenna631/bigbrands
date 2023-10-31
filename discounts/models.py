from django.db import models
from products.models import Product 


class Discount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    discount_percent = models.DecimalField(max_digits=6, decimal_places=2)
    active = models.BooleanField(default=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.discount_type} on {self.product.name}"

