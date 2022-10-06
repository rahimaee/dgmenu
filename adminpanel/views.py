from django.shortcuts import render


# Create your views here.

def index(request, *args, **kwargs):
    cx = {}
    return render(request, 'adminpanel/adminpanel_home_page.html', cx)
