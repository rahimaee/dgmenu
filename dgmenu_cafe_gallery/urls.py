from django.urls import path

from .views import cafe_gallery_page

app_name = 'dgmenu_cafe_gallery'
urlpatterns = [
    path('<cafename>/gallery/', cafe_gallery_page, name='gallery'),

]
