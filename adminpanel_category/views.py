from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
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
        category = FoodCategory.objects.filter(IsActiveAdmin=True, Cafe_id=cafe_id.id).all()

        ctx = {'category': category, }
        return render(request, 'adminpanel_category/category_list.html', ctx)


class CategoryCreate(LoginRequiredMixin, View):
    template = 'adminpanel_category/category_form.html'
    success_url = reverse_lazy('category:all')

    def get(self, request):
        form = CategoryForm()

        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = CategoryForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)
        fc = FoodCategory()
        user = request.user
        cafe_id = Cafe.objects.filter(Manager_id=user.id).first()
        fc.Cafe = cafe_id
        fc.NameFa = form.NameFa
        fc.NameEn = form.NameEn
        fc.IsActive = form.IsActive
        fc.IsActiveAdmin = True
        fc.save()
        return redirect(self.success_url)


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
        cat.cle = form.cleaned_data['NameEn']
        cat.NameFa = form.cleaned_data['NameFa']
        cat.Img = form.cleaned_data.get('Img')
        cat.IsActive = form.cleaned_data['IsActive']
        cat.save()
        return redirect(self.success_url)
