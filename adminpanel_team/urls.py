from django.urls import path
from . import views

app_name = 'team'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('create/', views.TeamCreate.as_view(), name='team_create'),
    path('<int:pk>/update/', views.TeamUpdate.as_view(), name='team_update'),
    # path('<int:pk>/delete/', views.GalleryDelete, name='Gallery_delete'),

]
