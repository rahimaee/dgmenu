from django.shortcuts import render


# Create your views here.

def home_page(request, *args, **kwargs):
    cx = {

    }
    return render(request, 'dgmenu_site_home/home_page.html', cx)
