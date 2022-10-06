from django.urls import path
from .views import index

app_name = 'adminpanel'
urlpatterns = [
    path('', index, name='starting_page'),

]
