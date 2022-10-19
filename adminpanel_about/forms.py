from django import forms


class ImageWidget(forms.widgets.ClearableFileInput):
    template_name = "adminpanel_food/custom_Img_file_input.html"


class AboutForm(forms.Form):
    Image = forms.ImageField(widget=ImageWidget,
                             label='عکس'
                             )
    Title = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", 'id': "Title"}),
        label='عنوان'
    )
    Description = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", 'id': "Description"}),
        label='توضیح کامل'

    )
