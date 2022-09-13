from django.shortcuts import render, Http404
from dgmenu_cafe.models import Cafe


# Create your views here.

def cafe_home_page(request, *args, **kwargs):
    cafe_name = str(request.path).split('/')[1]
    cafe = Cafe.objects.filter(Cafe_UserName=cafe_name).first()
    if cafe is None:
        raise Http404("کافه پیدا نشد")
    if cafe.Is_Active is True:
        raise Http404("کافه غیرفعال می باشد")
    cx = {'cafe': cafe,
          'CafeUserId': cafe.id}
    return render(request=request, template_name='dgmenu_cafe/cafe_home_page.html', context=cx)


def cafe_food_detail(request, *args, **kwargs):
    cx = {'CafeUserId': 12}
    print(request.path)
    return render(request=request, template_name='dgmenu_cafe/cafe_food_detail_page.html', context=cx)


def partial_view(request, *args, **kwargs):
    result = kwargs['CafeUserId']
    kwargs['result'] = result
    return render(request, 'shared/cafe/_HeaderReferences.html', kwargs)


def header_partial_view(request, *args, **kwargs):
    CafeUserId = kwargs['CafeUserId']
    cafe = Cafe.objects.filter(id=CafeUserId).first()
    if cafe is None:
        raise Http404("کافه پیدا نشد")
    if cafe.Is_Active is True:
        raise Http404("کافه غیرفعال می باشد")
    cx = {'cafe': cafe,
          'CafeUserId': cafe.id}
    return render(request, 'shared/cafe/_Header.html', cx)


def footer_partial_view(request, *args, **kwargs):
    CafeUserId = kwargs['CafeUserId']
    cafe = Cafe.objects.filter(id=CafeUserId).first()
    if cafe is None:
        raise Http404("کافه پیدا نشد")
    if cafe.Is_Active is True:
        raise Http404("کافه غیرفعال می باشد")
    cx = {'cafe': cafe,
          'CafeUserId': cafe.id}

    return render(request, 'shared/cafe/_Footer.html', cx)
