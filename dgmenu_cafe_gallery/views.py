from django.shortcuts import render, Http404
from dgmenu_cafe.models import Cafe
from .models import CafeGallery


# Create your views here.
def cafe_gallery_page(request, *args, **kwargs):
    cafe_name = str(request.path).split('/')[1]
    cafe = Cafe.objects.filter(Cafe_UserName=cafe_name).first()
    if cafe is None:
        raise Http404("کافه پیدا نشد")
    if cafe.Is_Active is True:
        raise Http404("کافه غیرفعال می باشد")
    PostGallery = CafeGallery.objects.filter(Cafe_id=cafe.id, IsActive=True, IsActiveAdmin=True).all()
    cx = {'cafe': cafe,
          'CafeUserId': cafe.id,
          'PostGallery': PostGallery}
    return render(request, 'dgmenu_cafe_gallery/cafe_gallery_page.html', cx)
