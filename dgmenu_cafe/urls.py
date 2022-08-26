from django.conf.urls import url
from django.urls import path

from .views import cafe_home_page, partial_view

app_name = 'dgmenu_cafe'
urlpatterns = [
    path('<cafename>/', cafe_home_page),

]
