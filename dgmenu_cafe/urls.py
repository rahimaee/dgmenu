from django.urls import path

from .views import cafe_home_page

app_name = 'dgmenu_cafe'
urlpatterns = [
    path('<cafename>/<s>', cafe_home_page),
]
