from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


RATES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_discounted_price(self):
        current_date = timezone.now().date()
        active_discounts = self.discount_set.filter(start_date__lte=current_date, end_date__gte=current_date, active=True)
        
        if active_discounts.exists():
            max_discount = active_discounts.order_by('-discount_percent').first()
            discounted_price = self.price - (self.price * max_discount.discount_percent / 100)
            return discounted_price
        else:
            return self.price


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(choices=RATES)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Review by {self.name} verified purchase"


class Discount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    discount_percent = models.DecimalField(max_digits=6, decimal_places=2)
    active = models.BooleanField(default=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.discount_type} on {self.product.name}"