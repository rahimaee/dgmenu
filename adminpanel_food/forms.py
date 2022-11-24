from django import forms
from django.forms.widgets import ClearableFileInput


class ImageWidget(forms.widgets.ClearableFileInput):
    template_name = "adminpanel_food/custom_Img_file_input.html"


class FoodForm(forms.Form):
    Image = forms.ImageField(widget=ImageWidget,
                             label='عکس اصلی',
                             )
    Title = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", 'id': "Title"}),
        label='نام محصول'
    )
    Description_Short = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 3, 'class': "form-control", 'id': "Description_Short", 'placeholder': "خلاصه توضیح محصول "}),
        label='توضیح کوتاه'
    )
    Description_Long = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'class': "form-control", 'id': "Description_Long", 'placeholder': "توضیح کامل محصول "}),
        label='توضیح کامل'
    )
    FoodCategory = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': "form-control"}),
        label='دسته بندی'
    )
    Ingredients = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", 'id': "Ingredients",
                   'placeholder': "مواد تشکیل دهنده را با استفاده از, بنویسید "}),
        label='مواد تشکیل دهنده'
    )
    Calories = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", 'id': "Calories", 'placeholder': "کالری(انرژی) محصول "}),
        label='کالری',
        required=False
    )
    Tag = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", 'id': "Tag", 'placeholder': "تگ ها را با استفاده از, بنویسید "}),
        label='برچسب'
    )
    Allergy = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", 'id': "Allergy", 'placeholder': "آلرژی را با استفاده از, بنویسید "}),
        label='آلرژی',
        required=False

    )
    Price = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", 'id': "Price", 'placeholder': "قیمت محصول به تومان "}),
        label='قیمت'
    )
    Discount = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", 'id': "Discount", 'placeholder': "قیمت تخفیف خورده محصول به تومان "}),
        label='قیمت با تخفیف',
        required=False
    )
    Is_Active = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={'type': "checkbox", 'name': "IsActive", 'id': "id_IsActive"}
        ),
        label='نمایش در سایت',
        required=False
    )
    Gallery_Img_1 = forms.ImageField(
        widget=ImageWidget,
        required=False,
        label='گالری محصول 1'
    )
    Gallery_Img_2 = forms.ImageField(
        widget=ImageWidget,
        required=False,
        label='گالری محصول 2'
    )
