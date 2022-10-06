from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from dgmenu_account.forms import LoginForm
from .models import CustomUser as User


def user_login_page(request):
    if request.user.is_authenticated:
        return redirect('adminpanel:starting_page')

    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        email = login_form.cleaned_data.get('email')
        print(email)
        password = login_form.cleaned_data.get('password')
        print(password)

        user = User.objects.filter(email=email).first()
        if user is not None:
            if user.check_password(password) is True:
                login(request, user)
        return redirect('adminpanel:starting_page')

    context = {
        'login_form': login_form
    }
    return render(request, 'dgmenu_account/login.html', context)

