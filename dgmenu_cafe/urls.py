from django.urls import path

from .views import cafe_home_page, cafe_food_detail

app_name = 'dgmenu_cafe'
urlpatterns = [
    path('<cafename>/', cafe_home_page),
    path('<cafename>/p/<id>', cafe_food_detail),

]
