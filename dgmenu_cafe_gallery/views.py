from django.shortcuts import render


# Create your views here.
def cafe_gallery_page(request, *args, **kwargs):
    cx = {
        'CafeUserId': 12
    }
    return render(request, 'dgmenu_cafe_gallery/cafe_gallery_page.html', cx)
