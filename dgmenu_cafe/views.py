from django.shortcuts import render


# Create your views here.

def cafe_home_page(request, *args, **kwargs):
    cx = {'CafeUserId': 12}
    print(request.path)
    return render(request=request, template_name='dgmenu_cafe/cafe_home_page.html', context=cx)


def partial_view(request, *args, **kwargs):
    result = kwargs['CafeUserId']
    kwargs['result'] = result
    return render(request, 'shared/cafe/_HeaderReferences.html', kwargs)


def header_partial_view(request, *args, **kwargs):
    result = kwargs['CafeUserId']
    kwargs['result'] = result
    return render(request, 'shared/cafe/_Header.html', kwargs)


def footer_partial_view(request, *args, **kwargs):
    result = kwargs['CafeUserId']
    kwargs['result'] = result
    return render(request, 'shared/cafe/_Footer.html', kwargs)
