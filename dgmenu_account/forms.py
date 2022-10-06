from django import forms
from .models import CustomUser as User


class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'email', 'class': 'form-control', 'id': 'validationCustom08',
                                      'placeholder': 'ایمیل خود را وارد کنید'}),
        label='ایمیل'

    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'type': 'password', 'id': 'validationCustom09', 'class': 'form-control', 'name': 'password',
                   'placeholder': 'رمز عبور را وارد کنید'}),
        label='رمز عبور'
    )

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_exists_user = User.objects.filter(username=user_name).exists()
        if is_exists_user is False:
            raise forms.ValidationError('کاربری با این ایمیل ثبت ثبت نشده')
        return user_name

    def clean_password(self):
        if len(self.cleaned_data.get('password')) < 4:
            raise forms.ValidationError("رمز عبور وارد شده کمتر از 4 کارکتر می باشد")
        return self.cleaned_data.get('password')
