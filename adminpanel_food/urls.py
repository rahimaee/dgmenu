from django.urls import path
from . import views
from django.views.generic import TemplateView

# from .views import save_data
app_name = 'food'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('main/create/', views.FoodCreate.as_view(), name='food_create'),
    path('main/<int:pk>/update/', views.FoodUpdate.as_view(), name='food_update'),
    path('main/<int:pk>/detail/', views.FoodDetail.as_view(), name='food_detail'),
    # # path('main/<int:pk>/delete/', views.AutoDelete.as_view(), name='auto_delete'),
    # path('url/', save_data, name='ss'),
]
