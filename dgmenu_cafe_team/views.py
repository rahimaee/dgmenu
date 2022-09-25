from django.shortcuts import render
from django.shortcuts import render, Http404
from dgmenu_cafe.models import Cafe
from dgmenu_cafe_gallery.models import CafeGallery


# Create your views here.

def cafe_team(request, *args, **kwargs):
    cafe_name = str(request.path).split('/')[1]
    cafe = Cafe.objects.filter(Cafe_UserName=cafe_name).first()
    if cafe is not None:
        Gallery = CafeGallery.objects.filter(Cafe_id=cafe.id, IsActive=True, IsActiveAdmin=True).all()
    else:
        raise Http404("مشکل دیتابیس")
    if cafe.Is_Active is True:
        raise Http404("کافه غیرفعال می باشد")
    cx = {'cafe': cafe,
          'CafeUserId': cafe.id, 'Gallery': Gallery}

    return render(request, 'dgmenu_cafe_team/cafe_team_page.html', cx)
