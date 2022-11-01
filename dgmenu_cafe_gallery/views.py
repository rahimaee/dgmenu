import uuid

from django.shortcuts import render, Http404
from dgmenu_cafe.models import Cafe
from dgmenu_cafe_viewers.models import ViewOfPage
from .models import CafeGallery
import datetime


# Create your views here.
def cafe_gallery_page(request, *args, **kwargs):
    cafe_name = str(request.path).split('/')[1]
    cafe = Cafe.objects.filter(Cafe_UserName=cafe_name).first()
    if cafe is None:
        raise Http404("کافه پیدا نشد")
    if cafe.Is_Active is True:
        raise Http404("کافه غیرفعال می باشد")
    PostGallery = CafeGallery.objects.filter(Cafe_id=cafe.id, IsActiveAdmin=True).all()
    cx = {'cafe': cafe,
          'CafeUserId': cafe.id,
          'PostGallery': PostGallery}
    res = render(request, 'dgmenu_cafe_gallery/cafe_gallery_page.html', cx)
    if request.COOKIES.get('uid'):
        uid = request.COOKIES.get('uid')
        view_of_page = ViewOfPage()
        view_of_page.Page = cafe.Cafe_UserName + "/gallery"
        view_of_page.Time = datetime.datetime.now()
        view_of_page.User = uid
        view_of_page.save()
    else:
        view_of_page = ViewOfPage()
        uid = uuid.uuid4().hex[:30]
        res.cookies.__setitem__('uid', uid)
        view_of_page.Page = cafe.Cafe_UserName + "/gallery"
        view_of_page.Time = datetime.datetime.now()
        view_of_page.User = uid
        view_of_page.save()
    return res
