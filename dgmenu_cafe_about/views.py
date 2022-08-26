from django.shortcuts import render


# Create your views here.

def cafe_about(request, *args, **kwargs):
    cx = {'CafeUserId': 12}
    return render(request, 'dgmenu_cafe_about/cafe_about_page.html', cx)
