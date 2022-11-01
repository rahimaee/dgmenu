from django.contrib.auth import login
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from dgmenu_account.forms import LoginForm
from .models import CustomUser as User

from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from .tokens import account_activation_token
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin


def user_login_page(request):
    if request.user.is_authenticated:
        return redirect('adminpanel:starting_page')
    login_form = LoginForm(request.POST or None)
    next = None
    if login_form.is_valid():
        email = login_form.cleaned_data.get('email')
        password = login_form.cleaned_data.get('password')
        user = User.objects.filter(email=email).first()
        if user is not None:
            if user.check_password(password) is True:
                login(request, user)
            else:
                login_form = LoginForm(request.POST or None)
                cx = {'ms': True, 'login_form': login_form}
                return render(request, 'dgmenu_account/login.html', cx)
            next = request.get_full_path().split('/?next=')
            if next.count == 2:
                next = next[1]
                domain = request.get_host()
                return redirect("http://" + domain + next)
            else:
                return redirect('adminpanel:starting_page')

    context = {
        'login_form': login_form
    }
    return render(request, 'dgmenu_account/login.html', context)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'dgmenu_account/login.html'
    email_template_name = 'dgmenu_account/password_reset_email.html'
    subject_template_name = 'dgmenu_account/email.html'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('account:login')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return render(request, 'dgmenu_account/account_confirm_email.html')
    else:
        return render(request, 'dgmenu_account/account_bad_link.html')
