from django.urls import path

from .views import cafe_home_page

app_name = 'dgmenu_cafe'
urlpatterns = [
    path('<cafename>/', cafe_home_page),
    path('<cafename>/<ss>', cafe_home_page),
]
