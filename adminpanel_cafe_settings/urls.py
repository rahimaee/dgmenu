from django.urls import path
from . import views

app_name = 'settings'
urlpatterns = [
    path('update/', views.SettingsUpdate.as_view(), name='settings_update'),
]
