from django.urls import path

from .views import home_page

app_name = 'dgmenu_site_home'
urlpatterns = [
    path('', home_page),

]
