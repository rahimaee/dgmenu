from django import forms


class ImageWidget(forms.widgets.ClearableFileInput):
    template_name = "adminpanel_food/custom_Img_file_input.html"


class CafeTabelForm(forms.Form):
    Img = forms.ImageField(
        widget=ImageWidget,
        label='عکس میز'
    )
    Name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", 'id': "Name"}),
        label='نام'
    )
    IsActive = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={'type': "checkbox", 'name': "IsActive", 'id': "id_IsActive"}
        ),
        label='نمایش در سایت',
        required=False
    )
