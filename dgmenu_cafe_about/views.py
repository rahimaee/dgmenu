from django.shortcuts import render, Http404
from dgmenu_cafe.models import Cafe
from dgmenu_cafe_about.models import CafeAbout


# Create your views here.

def cafe_about(request, *args, **kwargs):
    cafe_name = str(request.path).split('/')[1]
    cafe = Cafe.objects.filter(Cafe_UserName=cafe_name).first()
    if cafe is not None:
        about = CafeAbout.objects.filter(Cafe_id=cafe.id).first()
    else:
        raise Http404("مشکل دیتابیس")
    if cafe.Is_Active is True:
        raise Http404("کافه غیرفعال می باشد")
    cx = {'cafe': cafe,
          'CafeUserId': cafe.id, 'about': about}
    return render(request, 'dgmenu_cafe_about/cafe_about_page.html', cx)
