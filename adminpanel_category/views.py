import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseServerError, HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render

from dgmenu_cafe_viewers.models import ViewOfPage
from dgmenu_food_category.models import FoodCategory
from dgmenu_cafe.models import Cafe
from .forms import CategoryForm
import json
from dgmenu_food.models import Food
from dgmenu_account_role.models import Role


# Create your views here.

class MainView(LoginRequiredMixin, View):
    def get(self, request):
        role = Role.objects.filter(User_id=request.user.id, Cafe_category_view=True).first()
        if role is None:
            return HttpResponse("عدم دسترسیس")
        cafe_id = Cafe.objects.filter(id=role.Cafe.id, Admin_Is_Active=True).first()
        category = FoodCategory.objects.filter(IsActiveAdmin=True, Cafe_id=cafe_id.id).all().order_by('First')
        ctx = {'category': category, }
        return render(request, 'adminpanel_category/category_list.html', ctx)


class CategoryCreate(LoginRequiredMixin, View):
    template = 'adminpanel_category/category_form.html'
    success_url = reverse_lazy('category:all')

    def get(self, request):
        role = Role.objects.filter(User_id=request.user.id, Cafe_category_add=True).first()
        if role is None:
            return HttpResponse("عدم دسترسیس")
        form = CategoryForm(initial={'IsActive': True})

        ctx = {'form': form, 'cf': 'CategoryCreate'}
        return render(request, self.template, ctx)

    def post(self, request):
        role = Role.objects.filter(User_id=request.user.id, Cafe_category_add=True).first()
        if role is None:
            return HttpResponse("عدم دسترسیس")
        form = CategoryForm(request.POST, request.FILES or None)
        if not form.is_valid():
            ctx = {'form': form, 'cf': 'CategoryCreate'}
            return render(request, self.template, ctx)
        fc = FoodCategory()
        user = request.user
        cafe_id = Cafe.objects.filter(id=role.Cafe.id).first()
        count = FoodCategory.objects.filter(Cafe_id=cafe_id, IsActiveAdmin=True).all().count()
        fc.Cafe = cafe_id
        fc.NameFa = form.cleaned_data['NameFa']
        fc.NameEn = form.cleaned_data['NameEn']
        fc.IsActive = form.cleaned_data['IsActive']
        fc.Img = form.cleaned_data['Img']
        fc.IsActiveAdmin = True
        fc.First = count + 1
        fc.save()
        return redirect(self.success_url)


class CategoryDetail(LoginRequiredMixin, View):
    template = 'adminpanel_category/category_detail_view.html'

    def get(self, request, pk):
        role = Role.objects.filter(User_id=request.user.id, Cafe_category_view=True).first()
        if role is None:
            return HttpResponse("عدم دسترسیس")
        cat = FoodCategory.objects.filter(pk=pk, IsActiveAdmin=True).first()
        vpf = []
        vpft = 0
        vpfd = 0
        vpfm = 0
        vpfy = 0
        food = Food.objects.filter(FoodCategory_id=cat.id, Admin_Is_Active=True).all()
        for fd in food:
            t = '/' + fd.Cafe.Cafe_UserName + "/" + "p" + "/" + str(fd.id)
            vpf.append(t)
        for f in vpf:
            temp = ViewOfPage.objects.filter(Page=f).all().count()
            if temp is not None:
                vpft = vpft + temp
        for f in vpf:
            temp = ViewOfPage.objects.filter(Page=f, Time__day=datetime.datetime.now().day).all().count()
            if temp is not None:
                vpfd = vpfd + temp
        for f in vpf:
            temp = ViewOfPage.objects.filter(Page=f, Time__month=datetime.datetime.now().month).all().count()
            if temp is not None:
                vpfm = vpfm + temp
        for f in vpf:
            temp = ViewOfPage.objects.filter(Page=f, Time__year=datetime.datetime.now().year).all().count()
            if temp is not None:
                vpfy = vpfy + temp
        ctx = {'cat': cat, 'vpft': vpft, 'vpfd': vpfd, 'vpfm': vpfm, 'vpfy': vpfy}
        return render(request, self.template, ctx)


class CategoryUpdate(LoginRequiredMixin, View):
    success_url = reverse_lazy('category:all')
    template = 'adminpanel_category/category_form.html'

    def get(self, request, pk):
        role = Role.objects.filter(User_id=request.user.id, Cafe_category_edit=True).first()
        if role is None:
            return HttpResponse("عدم دسترسیس")
        cat = FoodCategory.objects.filter(pk=pk).first()
        form = CategoryForm(initial={'Img': cat.Img})
        form.initial["NameFa"] = cat.NameFa
        form.initial['NameEn'] = cat.NameEn
        form.initial['IsActive'] = cat.IsActive
        ctx = {'form': form, 'cf': 'CategoryUpdate', 'cat': cat}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        role = Role.objects.filter(User_id=request.user.id, Cafe_category_edit=True).first()
        if role is None:
            return HttpResponse("عدم دسترسیس")
        cat = FoodCategory.objects.filter(pk=pk).first()
        form = CategoryForm(request.POST, request.FILES or None, initial={'Img': cat.Img})
        if not form.is_valid():
            ctx = {'form': form, 'cf': 'CategoryUpdate', 'cat': cat}
            return render(request, self.template, ctx)
        cat.NameEn = form.cleaned_data['NameEn']
        cat.NameFa = form.cleaned_data['NameFa']
        cat.Img = form.cleaned_data.get('Img')
        cat.IsActive = form.cleaned_data['IsActive']
        cat.save()
        return redirect(self.success_url)


@csrf_exempt
def save_data(request):
    if request.user.is_authenticated:
        role = Role.objects.filter(User_id=request.user.id, Cafe_category_edit=True).first()
        if role is None:
            return HttpResponse("عدم دسترسیس")
        if request.method == 'POST':
            json_data = json.loads(request.body)
            data = json_data['data']
            data = list(data)
            for item in data:
                cat_id = str(item).split('_')[1]
                a_user = FoodCategory.objects.filter(Cafe__id=role.Cafe.id, pk=cat_id).first()
                if a_user is None:
                    return HttpResponse("error")
            temp = 1
            for item in data:
                cat_id = str(item).split('_')[1]
                cafe = Cafe.objects.filter(id=role.Cafe.id).first()
                f_cat_food = FoodCategory.objects.filter(pk=cat_id, Cafe_id=cafe.id, IsActiveAdmin=True).first()
                f_cat_food.First = temp
                temp = temp + 1
                f_cat_food.save()

    return HttpResponse("save")


@csrf_exempt
def CategoryDelete(request, *args, **kwargs):
    role = Role.objects.filter(User_id=request.user.id, Cafe_category_delete=True).first()
    if role is None:
        return HttpResponse("عدم دسترسیس")
    success_url = reverse_lazy('food:all')
    cat_id = kwargs.get('pk')
    if cat_id is not None:
        cat = FoodCategory.objects.filter(pk=cat_id, Cafe_id=role.Cafe.id).delete()
        return redirect(success_url)
    raise Http404()
