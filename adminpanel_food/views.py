from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View

from adminpanel_food.forms import FoodForm
from dgmenu_cafe.models import Cafe
from dgmenu_food.models import Food
from dgmenu_food_category.models import FoodCategory
import datetime


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        cafe_id = Cafe.objects.filter(Manager_id=user.id).first()
        food = Food.objects.filter(Cafe_id=cafe_id, Cafe__Manager_id=user.id, Admin_Is_Active=True)
        ctx = {'Food': food, }
        return render(request, 'adminpanel_food/food_list.html', ctx)


class FoodCreate(LoginRequiredMixin, View):
    template = 'adminpanel_food/food_form.html'
    success_url = reverse_lazy('food:all')

    def get(self, request):
        form = FoodForm(initial={'Is_Active': True})

        get_cat_food = FoodCategory.objects.filter(Cafe__Manager_id=request.user.id).all()
        get_cat_food_list = []
        for item in get_cat_food:
            get_cat_food_list.append((item.id, item.NameFa))
        form.fields['FoodCategory'].choices = get_cat_food_list
        form.fields['Image'].attrs = {'class': "custom-file-input"}
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = FoodForm(request.POST, request.FILES or None)
        get_cat_food = FoodCategory.objects.filter(Cafe__Manager_id=request.user.id).all()
        get_cat_food_list = []
        for item in get_cat_food:
            get_cat_food_list.append((item.id, item.NameFa))
        form.fields['FoodCategory'].choices = get_cat_food_list
        form.fields['Image'].attrs = {'class': "custom-file-input"}
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)
        fd = Food()
        user = request.user
        cafe = Cafe.objects.filter(Manager_id=user.id).first()
        count = Food.objects.filter(Cafe_id=cafe.id, Admin_Is_Active=True, Cafe__Manager_id=user.id).count()
        fd.Cafe = cafe
        fd.Image = form.cleaned_data['Image']
        fd.Title = form.cleaned_data['Title']
        fd.Description_Short = form.cleaned_data['Description_Short']
        fd.Description_Long = form.cleaned_data['Description_Long']
        fd.Ingredients = form.cleaned_data['Ingredients']
        fd.Calories = form.cleaned_data['Calories']
        fd.Tag = form.cleaned_data['Tag']
        fd.Allergy = form.cleaned_data['Allergy']
        fd.Price = form.cleaned_data['Price']
        fd.Discount = form.cleaned_data['Discount']
        fd.Admin_Is_Active = True
        fd.Is_Active = form.cleaned_data['Is_Active']
        fd.Submit_Time = datetime.datetime.now()
        fd.Last_Edit_Time = datetime.datetime.now()
        fd.First = count
        fd.save()
        return redirect(self.success_url)


class FoodDetail(LoginRequiredMixin, View):
    template = 'adminpanel_food/food_detail_view.html'

    def get(self, request, pk):
        food = Food.objects.filter(id=pk, Admin_Is_Active=True).first()
        ctx = {'food': food}
        return render(request, self.template, ctx)


class FoodUpdate(LoginRequiredMixin, View):
    success_url = reverse_lazy('food:all')
    template = 'adminpanel_food/food_form.html'

    def get(self, request, pk):
        fd = Food.objects.filter(pk=pk).first()
        form = FoodForm(initial={'Image': fd.Image, 'Is_Active': fd.Is_Active})
        get_cat_food = FoodCategory.objects.filter(Cafe__Manager_id=request.user.id).all()
        get_cat_food_list = []
        for item in get_cat_food:
            get_cat_food_list.append((item.id, item.NameFa))
        form.fields['FoodCategory'].choices = get_cat_food_list
        form.fields['FoodCategory'].initial = fd.FoodCategory_id
        form.initial['Title'] = fd.Title
        form.initial['Description_Short'] = fd.Description_Short
        form.initial['Description_Long'] = fd.Description_Long
        form.initial['Ingredients'] = fd.Ingredients
        form.initial['Calories'] = fd.Calories
        form.initial['Tag'] = fd.Tag
        form.initial['Allergy'] = fd.Allergy
        form.initial['Price'] = fd.Price
        form.initial['Discount'] = fd.Discount
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        fd = Food.objects.filter(id=pk).first()
        form = FoodForm(request.POST, request.FILES or None, initial={'Image': fd.Image, 'Is_Active': fd.Is_Active})
        get_cat_food = FoodCategory.objects.filter(Cafe__Manager_id=request.user.id).all()
        get_cat_food_list = []
        for item in get_cat_food:
            get_cat_food_list.append((item.id, item.NameFa))
        form.fields['FoodCategory'].choices = get_cat_food_list
        form.fields['FoodCategory'].initial = fd.FoodCategory_id
        if not form.is_valid():
            get_cat_food = FoodCategory.objects.filter(Cafe__Manager_id=request.user.id).all()
            get_cat_food_list = []
            for item in get_cat_food:
                get_cat_food_list.append((item.id, item.NameFa))
            form.fields['FoodCategory'].choices = get_cat_food_list
            form.fields['FoodCategory'].initial = fd.FoodCategory_id
            form.fields['Is_Active'].initial = fd.Is_Active
            ctx = {'form': form, }
            return render(request, self.template, ctx)

        fd.Title = form.cleaned_data['Title']
        fd.Image = form.cleaned_data['Image']
        fd.Description_Short = form.cleaned_data['Description_Short']
        fd.Description_Long = form.cleaned_data['Description_Long']
        cat = FoodCategory.objects.filter(id=form.cleaned_data['FoodCategory']).first()
        fd.FoodCategory = cat
        fd.Ingredients = form.cleaned_data['Ingredients']
        fd.Calories = form.cleaned_data['Calories']
        fd.Tag = form.cleaned_data['Tag']
        fd.Allergy = form.cleaned_data['Allergy']
        fd.Price = form.cleaned_data['Price']
        fd.Discount = form.cleaned_data['Discount']
        fd.Is_Active = form.cleaned_data['Is_Active']
        fd.save()
        return redirect(self.success_url)
