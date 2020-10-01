from django import forms
from mysite.models import *

class ShopForm(forms.ModelForm):
    class Meta:
        model=ShopData
        fields='__all__'