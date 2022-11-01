from django.urls import path

from .views import cafe_about

app_name = 'dgmenu_cafe_about'
urlpatterns = [
    path('<cafename>/about/', cafe_about, name='about'),

]
