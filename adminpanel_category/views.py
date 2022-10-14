from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseServerError, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from dgmenu_food_category.models import FoodCategory
from dgmenu_cafe.models import Cafe
from .forms import CategoryForm


# Create your views here.

class MainView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        cafe_id = Cafe.objects.filter(Manager_id=user.id).first()
        category = FoodCategory.objects.filter(IsActiveAdmin=True, Cafe_id=cafe_id.id).all().order_by('First')
        ctx = {'category': category, }
        return render(request, 'adminpanel_category/category_list.html', ctx)


class CategoryCreate(LoginRequiredMixin, View):
    template = 'adminpanel_category/category_form.html'
    success_url = reverse_lazy('category:all')

    def get(self, request):
        form = CategoryForm(initial={'IsActive': True})

        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = CategoryForm(request.POST, request.FILES or None)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)
        fc = FoodCategory()
        user = request.user
        cafe_id = Cafe.objects.filter(Manager_id=user.id).first()
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
        cat = FoodCategory.objects.filter(pk=pk, IsActiveAdmin=True).first()
        ctx = {'cat': cat}
        return render(request, self.template, ctx)


class CategoryUpdate(LoginRequiredMixin, View):
    success_url = reverse_lazy('category:all')
    template = 'adminpanel_category/category_form.html'

    def get(self, request, pk):
        cat = FoodCategory.objects.filter(pk=pk).first()
        form = CategoryForm(initial={'Img': cat.Img})
        form.initial["NameFa"] = cat.NameFa
        form.initial['NameEn'] = cat.NameEn
        form.initial['IsActive'] = cat.IsActive
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        cat = FoodCategory.objects.filter(pk=pk).first()
        form = CategoryForm(request.POST, request.FILES or None, initial={'Img': cat.Img})
        print(form)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)
        cat.NameEn = form.cleaned_data['NameEn']
        cat.NameFa = form.cleaned_data['NameFa']
        cat.Img = form.cleaned_data.get('Img')
        cat.IsActive = form.cleaned_data['IsActive']
        cat.save()
        return redirect(self.success_url)


import json


@csrf_exempt
def save_data(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            json_data = json.loads(request.body)
            data = json_data['data']
            data = list(data)
            for item in data:
                print(item)
                cat_id = str(item).split('_')[1]
                a_user = FoodCategory.objects.filter(Cafe__Manager_id=request.user.id, pk=cat_id).first()
                if a_user is None:
                    return HttpResponse("error")
                temp = 1
            for item in data:
                cat_id = str(item).split('_')[1]
                cat_order = str(item).split('_')[4]
                cafe = Cafe.objects.filter(Manager_id=request.user.id).first()
                f_cat_food = FoodCategory.objects.filter(pk=cat_id, Cafe_id=cafe.id, IsActiveAdmin=True).first()
                f_cat_food.First = temp
                temp = temp + 1
                f_cat_food.save()

    return HttpResponse("save")
