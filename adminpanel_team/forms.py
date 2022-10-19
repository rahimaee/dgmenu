from django import forms


class ImageWidget(forms.widgets.ClearableFileInput):
    template_name = "adminpanel_food/custom_Img_file_input.html"


class TeamForm(forms.Form):
    Profile = forms.ImageField(widget=ImageWidget,
                               label='عکس'

                               )
    Name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", 'id': "Name"}),
        label='نام'

    )
    Family = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", 'id': "Family"}),
        label='نام خانوادگی'

    )
    JobType = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", 'id': "JobType"}),
        label='شغل/سمت'

    )
    facebook = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", 'id': "facebook"}),
        label='فیس ‌بوک'

    )
    instagram = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", 'id': "instagram"}),
        label='ایسنتاگرام'

    )
    linkedin = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", 'id': "linkedin"}),
        label='لینکدین'

    )
    IsActive = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={'type': "checkbox", 'name': "IsActive", 'id': "IsActive"}
        ),
        label='نمایش در سایت',
        required=False
    )