from pyexpat import model
from django import forms
from .models import Product

class ProductModelForm(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"

