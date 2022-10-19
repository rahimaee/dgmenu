from django.urls import path
from . import views
from .views import save_data
app_name = 'category'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('create/', views.CategoryCreate.as_view(), name='category_create'),
    path('<int:pk>/update/', views.CategoryUpdate.as_view(), name='category_update'),
    path('<int:pk>/detail/', views.CategoryDetail.as_view(), name='category_detail'),
    path('<int:pk>/delete/', views.CategoryDelete, name='Category_delete'),
    path('sort/', save_data, name='category_sort'),
]
