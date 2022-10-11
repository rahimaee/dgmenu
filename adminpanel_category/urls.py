from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'category'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('main/create/', views.CategoryCreate.as_view(), name='category_create'),
    path('main/<int:pk>/update/', views.CategoryUpdate.as_view(), name='category_update'),
    # path('main/<int:pk>/delete/', views.AutoDelete.as_view(), name='auto_delete'),
]
