from django.urls import path
from . import views
from django.views.generic import TemplateView

# from .views import save_data
app_name = 'food'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('create/', views.FoodCreate.as_view(), name='food_create'),
    path('<int:pk>/update/', views.FoodUpdate.as_view(), name='food_update'),
    path('<int:pk>/detail/', views.FoodDetail.as_view(), name='food_detail'),
    path('<int:pk>/delete/', views.FoodDelete, name='food_delete'),
    path('sort/', views.save_data, name='food_sort'),
]
