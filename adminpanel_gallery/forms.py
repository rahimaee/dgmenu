from django import forms


class ImageWidget(forms.widgets.ClearableFileInput):
    template_name = "adminpanel_food/custom_Img_file_input.html"


class GalleryForm(forms.Form):
    Img = forms.ImageField(widget=ImageWidget,
                           label='عکس'

                           )
    Name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", 'id': "Name"}),
        label='نام'

    )
