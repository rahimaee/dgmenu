from dgmenu_food_category.models import FoodCategory
from django import forms


class ImageWidget(forms.widgets.ClearableFileInput):
    template_name = "adminpanel_food/custom_Img_file_input.html"


class CategoryForm(forms.Form):
    Img = forms.ImageField(
        widget=ImageWidget,
        label='ایکون'
    )
    NameFa = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", 'id': "NameFa"}),
        label='نام فارسی'
    )
    NameEn = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", 'id': "NameEn"}),
        label='نام انگلیسی'

    )
    IsActive = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={'type': "checkbox", 'name': "IsActive", 'id': "id_IsActive"}
        ),
        label='نمایش در سایت',
        required=False
    )
