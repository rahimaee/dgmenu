import datetime
import uuid

from django.http import Http404
from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import CafeTabel
from dgmenu_cafe.models import Cafe
from dgmenu_cafe_gallery.models import CafeGallery
from dgmenu_cafe_viewers.models import ViewOfPage


# Create your views here.


def cate_tabel(request, *args, **kwargs):
    cafe_name = str(request.path).split('/')[1]
    print(request.path)
    cafe = Cafe.objects.filter(Cafe_UserName=cafe_name, Admin_Is_Active=True).first()
    if cafe is None:
        raise Http404("کافه پیدا نشد")
    UnId = kwargs.get('UnId')
    if UnId is None:
        raise Http404()
    tabel = CafeTabel.objects.filter(UnId=UnId, Cafe_id=cafe.id).first()
    res = redirect('dgmenu_cafe:cafe_home', cafename=str(cafe.Cafe_UserName))
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
    if request.COOKIES.get('tbl'):
        res.cookies.__setitem__('tbl', tabel.id)
    else:
        res.cookies.__setitem__('tbl', tabel.id)
    return res
