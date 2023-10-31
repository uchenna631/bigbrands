from django import forms
from .models import Discount


class DiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = ['product', 'name', 'discount_percent', 'start_date', 'end_date', 'active']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
