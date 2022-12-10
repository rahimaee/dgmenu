import datetime
import uuid

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from dgmenu_cafe_tabel.models import CafeTabel
from dgmenu_account_role.models import Role
from .forms import CafeTabelForm
from dgmenu_cafe.models import Cafe
from dgmenu_cafe_viewers.models import ViewOfPage


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        if user is None:
            raise Http404()
        role = Role.objects.filter(User_id=user.id).first()
        if role is None:
            raise Http404()
        cafe_tabel = CafeTabel.objects.filter(Cafe_id=role.Cafe.id, IsActiveAdmin=True).all()
        ctx = {'cafe_tabel': cafe_tabel, }
        return render(request, 'adminpanel_cafe_tabel/cafe_tabel_list.html', ctx)


class CafeTabelCreate(LoginRequiredMixin, View):
    template = 'adminpanel_cafe_tabel/cafe_tabel_form.html'
    success_url = reverse_lazy('cafe_tabel:all')

    def get(self, request):
        role = Role.objects.filter(User_id=request.user.id).first()
        if role is None:
            return HttpResponse("عدم دسترسیس")
        form = CafeTabelForm(initial={'IsActive': True})

        ctx = {'form': form, 'cf': 'CafeTabelCreate'}
        return render(request, self.template, ctx)

    def post(self, request):
        role = Role.objects.filter(User_id=request.user.id).first()
        if role is None:
            return HttpResponse("عدم دسترسیس")
        form = CafeTabelForm(request.POST, request.FILES or None)
        if not form.is_valid():
            ctx = {'form': form, 'cf': 'CafeTabelCreate'}
            return render(request, self.template, ctx)
        ft = CafeTabel()
        cafe = Cafe.objects.filter(id=role.Cafe.id).first()
        ft.Cafe = cafe
        ft.Name = form.cleaned_data['Name']
        ft.IsActive = form.cleaned_data['IsActive']
        ft.Img = form.cleaned_data['Img']
        ft.UnId = uuid.uuid4().hex
        ft.IsActiveAdmin = True
        ft.save()
        return redirect(self.success_url)


class CafeTabelDetail(LoginRequiredMixin, View):
    template = 'adminpanel_cafe_tabel/cafe_tabel_detail_view.html'

    def get(self, request, pk):
        role = Role.objects.filter(User_id=request.user.id).first()
        if role is None:
            return HttpResponse("عدم دسترسیس")
        cafe_tabel = CafeTabel.objects.filter(pk=pk, IsActiveAdmin=True).first()
        tabel_path = '/' + role.Cafe.Cafe_UserName + "/" + "tabel" + "/" + str(cafe_tabel.UnId)

        vpft = ViewOfPage.objects.filter(Page=tabel_path).all().count()
        vpfd = ViewOfPage.objects.filter(Page=tabel_path, Time__day=datetime.datetime.now().day).all().count()
        vpfm = ViewOfPage.objects.filter(Page=tabel_path, Time__month=datetime.datetime.now().month).all().count()
        vpfy = ViewOfPage.objects.filter(Page=tabel_path, Time__year=datetime.datetime.now().year).all().count()
        ctx = {'cafe_tabel': cafe_tabel, 'vpft': vpft, 'vpfd': vpfd, 'vpfm': vpfm, 'vpfy': vpfy}
        return render(request, self.template, ctx)


class CafeTabelUpdate(LoginRequiredMixin, View):
    success_url = reverse_lazy('adminpanel_cafe_tabel:all')
    template = 'adminpanel_cafe_tabel/cafe_tabel_form.html'

    def get(self, request, pk):
        role = Role.objects.filter(User_id=request.user.id).first()
        if role is None:
            return HttpResponse("عدم دسترسیس")
        cafe_tabel = CafeTabel.objects.filter(pk=pk).first()
        form = CafeTabelForm(initial={'Img': cafe_tabel.Img})
        form.initial["Name"] = cafe_tabel.Name
        form.initial['IsActive'] = cafe_tabel.IsActive
        ctx = {'form': form, 'cf': 'CafeTabelUpdate', 'cafe_tabel': cafe_tabel}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        role = Role.objects.filter(User_id=request.user.id).first()
        if role is None:
            return HttpResponse("عدم دسترسیس")
        cafe_tabel = CafeTabel.objects.filter(pk=pk).first()
        form = CafeTabelForm(request.POST, request.FILES or None, initial={'Img': cafe_tabel.Img})
        if not form.is_valid():
            ctx = {'form': form, 'cf': 'CafeTabelUpdate', 'cafe_tabel': cafe_tabel}
            return render(request, self.template, ctx)
        cafe_tabel.Name = form.cleaned_data['Name']
        cafe_tabel.Img = form.cleaned_data.get('Img')
        cafe_tabel.IsActive = form.cleaned_data['IsActive']
        cafe_tabel.save()
        return redirect(self.success_url)


@csrf_exempt
def CafeTabelDelete(request, *args, **kwargs):
    role = Role.objects.filter(User_id=request.user.id).first()
    if role is None:
        return HttpResponse("عدم دسترسیس")
    success_url = reverse_lazy('food:all')
    tabel_id = kwargs.get('pk')
    if tabel_id is not None:
        cafe_tabel = CafeTabel.objects.filter(pk=tabel_id, Cafe_id=role.Cafe.id).delete()
        return redirect(success_url)
    raise Http404()
