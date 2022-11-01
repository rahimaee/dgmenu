import uuid

from django.shortcuts import render
from django.shortcuts import render, Http404
from dgmenu_cafe.models import Cafe
from dgmenu_cafe_viewers.models import ViewOfPage
from .models import CafeTeam
import datetime


# Create your views here.

def cafe_team(request, *args, **kwargs):
    cafe_name = str(request.path).split('/')[1]
    cafe = Cafe.objects.filter(Cafe_UserName=cafe_name).first()
    if cafe is not None:
        Cafe_Team = CafeTeam.objects.filter(Cafe_id=cafe.id, IsActive=True, IsActiveAdmin=True).all()
    else:
        raise Http404("مشکل دیتابیس")
    if cafe.Is_Active is True:
        raise Http404("کافه غیرفعال می باشد")

    cx = {'cafe': cafe,
          'CafeUserId': cafe.id, 'Cafe_Team': Cafe_Team}
    res = render(request, 'dgmenu_cafe_team/cafe_team_page.html', cx)
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
