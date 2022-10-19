from django.urls import path
from . import views

app_name = 'gallery'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('create/', views.GalleryCreate.as_view(), name='Gallery_create'),
    path('<int:pk>/update/', views.GalleryUpdate.as_view(), name='Gallery_update'),
    path('<int:pk>/delete/', views.GalleryDelete, name='Gallery_delete'),

]
