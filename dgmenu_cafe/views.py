from django.shortcuts import render, Http404
from dgmenu_cafe.models import Cafe
from dgmenu_cafe_gallery.models import CafeGallery
from dgmenu_food_category.models import FoodCategory
from dgmenu_food.models import Food


# Create your views here.

def cafe_home_page(request, *args, **kwargs):
    cafe_name = str(request.path).split('/')[1]
    cafe = Cafe.objects.filter(Cafe_UserName=cafe_name).first()
    if cafe is None:
        raise Http404("کافه پیدا نشد")
    if cafe.Is_Active is True:
        raise Http404("کافه غیرفعال می باشد")
    category = FoodCategory.objects.filter(Cafe_id=cafe.id, IsActive=True, IsActiveAdmin=True).all()
    if category is not None:
        category = category.order_by('First')
    food = Food.objects.filter(Cafe_id=cafe.id, Is_Active=True, Admin_Is_Active=True).all()

    cx = {'cafe': cafe,
          'CafeUserId': cafe.id,
          'category': category,
          'food': food}
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
    cafe_gallery = CafeGallery.objects.filter(Cafe_id=cafe.id, IsActive=True, IsActiveAdmin=True).all()
    cafe_gallery = cafe_gallery[:5]
    cx = {'cafe': cafe,
          'CafeUserId': cafe.id,
          'cafe_gallery': cafe_gallery}

    return render(request, 'shared/cafe/_Footer.html', cx)
