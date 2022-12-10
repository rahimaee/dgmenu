from django.urls import path
from . import views


app_name = 'cafe_tabel'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('create/', views.CafeTabelCreate.as_view(), name='cafe_tabel_create'),
    path('<int:pk>/update/', views.CafeTabelUpdate.as_view(), name='cafe_tabel_update'),
    path('<int:pk>/detail/', views.CafeTabelDetail.as_view(), name='cafe_tabel_detail'),
    path('<int:pk>/delete/', views.CafeTabelDelete, name='cafe_tabel_delete'),
]
