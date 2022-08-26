from django.urls import path

from .views import cafe_team

app_name = 'dgmenu_cafe_team'
urlpatterns = [
    path('<cafename>/team', cafe_team),

]
