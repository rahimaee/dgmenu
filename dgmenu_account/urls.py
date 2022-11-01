from django.urls import path, reverse_lazy

from .views import user_login_page, activate
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('login/', user_login_page, name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='dgmenu_site_home/home_page.html'), name='logout'),
    path('activate/<uidb64>/<token>', activate, name='activate'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='dgmenu_account/password_reset_form.html',
                                              email_template_name='dgmenu_account/password_reset_email.html',
                                              success_url=reverse_lazy('account:password_reset_done')),
         name='password_reset'),

    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='dgmenu_account/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="dgmenu_account/password_reset_confirm.html",
                                                     success_url=reverse_lazy('account:password_reset_complete')),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='dgmenu_account/password_reset_complete.html'),
         name='password_reset_complete'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
]
