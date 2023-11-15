from django import forms
from .models import Product, Category, Review, Discount


class ProductForm(forms.ModelForm):
    '''Product form to add/update products'''

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    ''' Product review form form'''
    class Meta:
        model = Review
        fields = ('title', 'text', 'rating')


class DiscountForm(forms.ModelForm):
    ''' Product discount form'''
    class Meta:
        model = Discount
        fields = ['product', 'name', 'discount_percent', 'start_date', 'end_date', 'active']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
