from django.shortcuts import render, Http404, HttpResponse
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
    food = food.order_by('First')
    cx = {'cafe': cafe,
          'CafeUserId': cafe.id,
          'category': category,
          'food': food}
    return render(request=request, template_name='dgmenu_cafe/cafe_home_page.html', context=cx)


def cafe_food_detail(request, *args, **kwargs):
    cafe_name = str(request.path).split('/')[1]
    cafe = Cafe.objects.filter(Cafe_UserName=cafe_name).first()
    food_id = kwargs.get('id')
    if cafe is None:
        raise Http404("کافه پیدا نشد")
    if cafe.Is_Active is True:
        raise Http404("کافه غیرفعال می باشد")
    category = FoodCategory.objects.filter(Cafe_id=cafe.id, IsActive=True, IsActiveAdmin=True).all()
    if category is not None:
        category = category.order_by('First')
    food = Food.objects.filter(Cafe_id=cafe.id, Is_Active=True, Admin_Is_Active=True, pk=food_id).first()
    if food is None:
        raise Http404("خطا دیتابیس")

    food_suggestion = Food.objects.filter(FoodCategory_id=food.FoodCategory_id, Is_Active=True,
                                          Admin_Is_Active=True).all()
    if food_suggestion is not None:
        food_suggestion = food_suggestion.order_by(
            'pk')[:4]

    cx = {'cafe': cafe,
          'CafeUserId': cafe.id,
          'category': category,
          'food': food,
          'food_suggestion': food_suggestion}
    return render(request=request, template_name='dgmenu_cafe/cafe_food_detail_page.html', context=cx)


def partial_view(request, *args, **kwargs):
    result = kwargs['CafeUserId']
    kwargs['result'] = result
    return render(request, 'shared/cafe/_HeaderReferences.html', kwargs)


def header_partial_view(request, *args, **kwargs):
    CafeUserId = kwargs['CafeUserId']
    cafe = Cafe.objects.filter(id=CafeUserId).first()
    url1 = request.build_absolute_uri().split('/')[0]
    url2 = request.build_absolute_uri().split('/')[2]
    if cafe is None:
        raise Http404("کافه پیدا نشد")
    if cafe.Is_Active is True:
        raise Http404("کافه غیرفعال می باشد")
    url = url1 + '//' + url2 + "/" + cafe.Cafe_UserName
    print("my url :" + url)
    cx = {'cafe': cafe,
          'CafeUserId': cafe.id,
          'url': url}
    return render(request, 'shared/cafe/_Header.html', cx)


def footer_partial_view(request, *args, **kwargs):
    CafeUserId = kwargs['CafeUserId']
    cafe = Cafe.objects.filter(id=CafeUserId).first()
    if cafe is None:
        raise Http404("کافه پیدا نشد")
    if cafe.Is_Active is True:
        raise Http404("کافه غیرفعال می باشد")
    cafe_gallery = CafeGallery.objects.filter(Cafe_id=cafe.id, IsActiveAdmin=True).all()
    cafe_gallery = cafe_gallery[:5]
    WorkTime = list()
    if cafe.Cafe_Opening_Hours is not None:
        WorkTime = cafe.Cafe_Opening_Hours.split('،')

    cx = {'cafe': cafe,
          'CafeUserId': cafe.id,
          'cafe_gallery': cafe_gallery,
          'WorkTime': WorkTime}

    return render(request, 'shared/cafe/_Footer.html', cx)
