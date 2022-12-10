import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt

from adminpanel_gallery.forms import GalleryForm
from dgmenu_cafe.models import Cafe
from dgmenu_cafe_gallery.models import CafeGallery
# Create your views here.
from django.views import View
from dgmenu_account_role.models import Role


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        role = Role.objects.filter(User_id=request.user.id, Cafe_gallery_view=True).first()
        if role is None:
            return HttpResponse("عدم دسترسیس")
        cafe_gallery = CafeGallery.objects.filter(Cafe_id=role.Cafe.id, IsActiveAdmin=True).all().order_by(
            'TimeUpload')
        ctx = {'gallery': cafe_gallery, }
        return render(request, 'adminpanel_gallery/gallery_list.html', ctx)


class GalleryCreate(LoginRequiredMixin, View):
    template = 'adminpanel_gallery/gallery_form.html'
    success_url = reverse_lazy('gallery:all')

    def get(self, request):
        role = Role.objects.filter(User_id=request.user.id, Cafe_gallery_add=True).first()
        if role is None:
            return HttpResponse("عدم دسترسیس")
        form = GalleryForm()

        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        role = Role.objects.filter(User_id=request.user.id, Cafe_gallery_add=True).first()
        if role is None:
            return HttpResponse("عدم دسترسیس")
        form = GalleryForm(request.POST, request.FILES or None)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        user = request.user
        cafe_gallery = CafeGallery()
        cafe = Cafe.objects.filter(id=role.Cafe.id).first()
        cafe_gallery.Cafe = cafe
        cafe_gallery.Img = form.cleaned_data['Img']
        cafe_gallery.Name = form.cleaned_data['Name']
        cafe_gallery.TimeUpload = datetime.datetime.now()
        cafe_gallery.IsActiveAdmin = True
        cafe_gallery.save()
        return redirect(self.success_url)


class GalleryUpdate(LoginRequiredMixin, View):
    success_url = reverse_lazy('category:all')
    template = 'adminpanel_gallery/gallery_form.html'

    def get(self, request, pk):
        role = Role.objects.filter(User_id=request.user.id, Cafe_gallery_edit=True).first()
        if role is None:
            return HttpResponse("عدم دسترسیس")
        cafe_gallery = CafeGallery.objects.filter(pk=pk, Cafe_id=role.Cafe.id).first()
        if cafe_gallery is None:
            raise Http404()
        form = GalleryForm(initial={'Img': cafe_gallery.Img})
        form.initial["Name"] = cafe_gallery.Name
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        role = Role.objects.filter(User_id=request.user.id, Cafe_gallery_add=True).first()
        if role is None:
            return HttpResponse("عدم دسترسیس")
        cafe_gallery = CafeGallery.objects.filter(pk=pk, Cafe_id=role.Cafe.id).first()
        form = GalleryForm(request.POST, request.FILES or None, initial={'Img': cafe_gallery.Img})
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)
        cafe_gallery.Img = form.cleaned_data['Img']
        cafe_gallery.Name = form.cleaned_data['Name']
        cafe_gallery.save()
        return redirect(self.success_url)


@csrf_exempt
def GalleryDelete(request, *args, **kwargs):
    role = Role.objects.filter(User_id=request.user.id, Cafe_gallery_delete=True).first()
    if role is None:
        return HttpResponse("عدم دسترسیس")
    success_url = reverse_lazy('gallery:all')
    gallery_id = kwargs.get('pk')
    if gallery_id is not None:
        gallery = CafeGallery.objects.filter(pk=gallery_id, Cafe_id=role.Cafe.id).delete()
        return redirect(success_url)
    raise Http404()
