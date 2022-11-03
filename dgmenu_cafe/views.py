import datetime

from django.shortcuts import render, Http404, HttpResponse
from dgmenu_cafe.models import Cafe
from dgmenu_cafe_gallery.models import CafeGallery
from dgmenu_food_category.models import FoodCategory
from dgmenu_food.models import Food
from dgmenu_cafe_viewers.models import ViewOfPage
import uuid


# Create your views here.

def cafe_home_page(request, *args, **kwargs):
    cafe_name = str(request.path).split('/')[1]
    cafe = Cafe.objects.filter(Cafe_UserName=cafe_name).first()
    if cafe is None:
        raise Http404("کافه پیدا نشد")
    if cafe.Is_Active is False:
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
    res = render(request=request, template_name='dgmenu_cafe/cafe_home_page.html', context=cx)
    if request.COOKIES.get('uid'):
        uid = request.COOKIES.get('uid')
        view_of_page = ViewOfPage()
        view_of_page.Page = request.path
        view_of_page.Time = datetime.datetime.now()
        view_of_page.User = uid
        view_of_page.save()
    else:
        view_of_page = ViewOfPage()
        uid = uuid.uuid4().hex[:30]
        res.cookies.__setitem__('uid', uid)
        view_of_page.Page = request.path
        view_of_page.Time = datetime.datetime.now()
        view_of_page.User = uid
        view_of_page.save()
    return res


def cafe_food_detail(request, *args, **kwargs):
    cafe_name = str(request.path).split('/')[1]
    cafe = Cafe.objects.filter(Cafe_UserName=cafe_name).first()
    food_id = kwargs.get('id')
    if cafe is None:
        raise Http404("کافه پیدا نشد")
    if cafe.Is_Active is False:
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
    gallery = []
    if food.Gallery_Image_1 is not None:
        gallery.append(food.Gallery_Image_1)
    if food.Gallery_Image_2 is not None:
        gallery.append(food.Gallery_Image_2)
    if food.Gallery_Image_3 is not None:
        gallery.append(food.Gallery_Image_3)
    cx = {'cafe': cafe,
          'CafeUserId': cafe.id,
          'category': category,
          'food': food,
          'food_suggestion': food_suggestion,
          'gallery': gallery}
    res = render(request=request, template_name='dgmenu_cafe/cafe_food_detail_page.html', context=cx)
    if request.COOKIES.get('uid'):
        uid = request.COOKIES.get('uid')
        view_of_page = ViewOfPage()
        view_of_page.Page = request.path
        view_of_page.Time = datetime.datetime.now()
        view_of_page.User = uid
        view_of_page.save()
    else:
        view_of_page = ViewOfPage()
        uid = uuid.uuid4().hex[:30]
        res.cookies.__setitem__('uid', uid)
        view_of_page.Page = request.path
        view_of_page.Time = datetime.datetime.now()
        view_of_page.User = uid
        view_of_page.save()
    return res


def partial_view(request, *args, **kwargs):
    CafeUserId = kwargs['CafeUserId']
    cafe = Cafe.objects.filter(id=CafeUserId).first()
    url1 = request.build_absolute_uri().split('/')[0]
    url2 = request.build_absolute_uri().split('/')[2]
    if cafe is None:
        raise Http404("کافه پیدا نشد")
    if cafe.Is_Active is False:
        raise Http404("کافه غیرفعال می باشد")
    cx = {'cafe': cafe}
    return render(request, 'shared/cafe/_HeaderReferences.html', cx)


def header_partial_view(request, *args, **kwargs):
    CafeUserId = kwargs['CafeUserId']
    cafe = Cafe.objects.filter(id=CafeUserId).first()
    url1 = request.build_absolute_uri().split('/')[0]
    url2 = request.build_absolute_uri().split('/')[2]
    if cafe is None:
        raise Http404("کافه پیدا نشد")
    if cafe.Is_Active is False:
        raise Http404("کافه غیرفعال می باشد")
    url = url1 + '//' + url2 + "/" + cafe.Cafe_UserName
    cx = {'cafe': cafe,
          'CafeUserId': cafe.id,
          'url': url}
    return render(request, 'shared/cafe/_Header.html', cx)


def footer_partial_view(request, *args, **kwargs):
    CafeUserId = kwargs['CafeUserId']
    cafe = Cafe.objects.filter(id=CafeUserId).first()
    if cafe is None:
        raise Http404("کافه پیدا نشد")
    if cafe.Is_Active is False:
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
