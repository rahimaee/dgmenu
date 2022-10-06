from django.urls import path

from .views import user_login_page
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('login', user_login_page, name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='dgmenu_site_home/home_page.html'), name='logout'),
]
