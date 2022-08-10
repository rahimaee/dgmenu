from django.shortcuts import render


# Create your views here.

def cafe_home_page(request, *args, **kwargs):
    ct = {}
    print(request.path)
    print(kwargs['cafename'])
    return render(request=request, template_name='dgmenu_cafe/cafe_home_page.html', context=ct)
