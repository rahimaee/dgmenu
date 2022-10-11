from dgmenu_food_category.models import FoodCategory
from django import forms


class CategoryForm(forms.Form):
    Img = forms.ImageField(
        label='عکس'

    )
    NameFa = forms.CharField(
        widget=forms.TextInput(
            attrs={}),
        label='نام فارسی'
    )
    NameEn = forms.CharField(
        widget=forms.TextInput(
            attrs={}),
        label='نام فارسی'
    )
    IsActive = forms.BooleanField(
        label='فعال/غیرفعال'
    )
