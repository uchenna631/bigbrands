from django.db import models
from checkout.models import Order
from django.contrib.auth.models import User
from django.utils import timezone


class OrderManager(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    processed = models.BooleanField(default=False)
    processed_by = models.CharField(max_length=120, blank=True)
    processed_date = models.DateTimeField(auto_now_add=False, blank=True)
    delivered = models.BooleanField(default=False)
    delivered_by = models.CharField(max_length=120, blank=True)
    delivered_date = models.DateTimeField(auto_now_add=False, blank=True)
    status = models.CharField(max_length=80, blank=True)

    def save(self, *args, **kwargs):
        # check if it's a new instance and if processed is set
        if not self.pk and self.processed:
            self.processed_date = timezone.now()
            self.processed_by = models.ForeignKey(
                User, on_delete=models.SET_NULL)
        if not self.pk and self.delivered:
            self.delivery_date = timezone.now()
            self.delivered_by = models.ForeignKey(
                User, on_delete=models.SET_NULL)
        super().save(*args, **kwargs)