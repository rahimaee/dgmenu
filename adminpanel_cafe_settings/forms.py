from django import forms


class ImageWidget(forms.widgets.ClearableFileInput):
    template_name = "adminpanel_food/custom_Img_file_input.html"


class SettingsForm(forms.Form):
    Cafe_Name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", 'id': "Cafe_Name"}),
        label='نام کافه'
    )
    Cafe_Description = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", 'id': "Cafe_Description"}),
        label='توضیح کافه'

    )
    Cafe_keywords = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", 'id': "Cafe_Description"}),
        label='کلمات کیدی'

    )
    Cafe_Address = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", 'id': "Cafe_Address"}),
        label='ادرس کافه',

    )
    Cafe_Tel1 = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", 'id': "Cafe_Tel1"}),
        label='شماره تماس1'

    )
    Cafe_Tel2 = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", 'id': "Cafe_Tel2"}),
        label='شماره تماس2'

    )
    Cafe_Tel3 = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", 'id': "Cafe_Tel3"}),
        label='شماره تماس3'

    )
    Cafe_Email = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", 'id': "Cafe_Email"}),
        label='ادرس ایمیل'

    )
    Cafe_Instagram = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", 'id': "Cafe_Instagram"}),
        label='اینستاگرام',
        required=False

    )
    Cafe_Facebook = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", 'id': "Cafe_Facebook"}),
        label='فیس بوک',
        required=False

    )
    Cafe_YouTube = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", 'id': "Cafe_YouTube"}),
        label='یوتیوب',
        required=False

    )
    Cafe_Twitter = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", 'id': "Cafe_Twitter"}),
        label='توتیتر',
        required=False

    )
    Cafe_Opening_Hours = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", 'id': "Cafe_Opening_Hours"}),
        label='ساعت کاری',
        required=False

    )
    Cafe_Header_Logo = forms.ImageField(widget=ImageWidget,
                                        label='لوگو هدر'
                                        )
    Cafe_favicon = forms.ImageField(widget=ImageWidget,
                                    label='favicon'
                                    )
    Cafe_Apple_Touch_Icon57 = forms.ImageField(widget=ImageWidget,
                                               label='Icon57'
                                               )
    Cafe_Apple_Touch_Icon60 = forms.ImageField(widget=ImageWidget,
                                               label='Icon60'
                                               )

    Cafe_Apple_Touch_Icon72 = forms.ImageField(widget=ImageWidget,
                                               label='Icon72'
                                               )
    Cafe_Apple_Touch_Icon76 = forms.ImageField(widget=ImageWidget,
                                               label='Icon76'
                                               )
    Cafe_Apple_Touch_Icon114 = forms.ImageField(widget=ImageWidget,
                                                label='Icon114'
                                                )
    Cafe_Apple_Touch_Icon120 = forms.ImageField(widget=ImageWidget,
                                                label='Icon120'
                                                )
    Cafe_Apple_Touch_Icon144 = forms.ImageField(widget=ImageWidget,
                                                label='Icon144'
                                                )
    Cafe_Apple_Touch_Icon152 = forms.ImageField(widget=ImageWidget,
                                                label='Icon152'
                                                )
    Cafe_Apple_Touch_Icon180 = forms.ImageField(widget=ImageWidget,
                                                label='Icon180'
                                                )
    Cafe_Apple_Touch_Icon192 = forms.ImageField(widget=ImageWidget,
                                                label='Icon192'
                                                )
    Cafe_Apple_Touch_Icon196 = forms.ImageField(widget=ImageWidget,
                                                label='Icon196'
                                                )

    Cafe_Apple_Touch_Icon16 = forms.ImageField(widget=ImageWidget,
                                               label='Icon16'
                                               )
    Cafe_Apple_Touch_Icon32 = forms.ImageField(widget=ImageWidget,
                                               label='Icon32'
                                               )
    Cafe_Msapplication = forms.ImageField(widget=ImageWidget,
                                          label='Msapplication'
                                          )
    Cafe_Header_Home_Background = forms.ImageField(widget=ImageWidget,
                                                   label='عکس بنر سقحه اصلی'
                                                   )
    Cafe_Header_Detail_Background = forms.ImageField(widget=ImageWidget,
                                                     label='عکس بنر محصول'
                                                     )
    Cafe_Header_About_Background = forms.ImageField(widget=ImageWidget,
                                                    label='عکس بنر سقحه درباره ما'
                                                    )
    Cafe_Header_Team_Background = forms.ImageField(widget=ImageWidget,
                                                   label='عکس بنر سقحه تیم'
                                                   )
    Cafe_Banner_Home = forms.ImageField(widget=ImageWidget,
                                        label='عکس بنر سقحه کافه'
                                        )
