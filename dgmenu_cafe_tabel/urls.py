from django.urls import path
from .views import cate_tabel
app_name = 'dgmenu_cafe_tabel'
urlpatterns = [
    path('<cafename>/tabel/<UnId>', cate_tabel, name='tabel'),
]
