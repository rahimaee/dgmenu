import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from adminpanel_food.forms import FoodForm
from dgmenu_cafe.models import Cafe
from dgmenu_food.models import Food
from dgmenu_food_category.models import FoodCategory
import datetime
from dgmenu_cafe_viewers.models import ViewOfPage


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        cafe_id = Cafe.objects.filter(Manager_id=user.id).first()
        food = Food.objects.filter(Cafe_id=cafe_id, Cafe__Manager_id=user.id, Admin_Is_Active=True).order_by('First')
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
        ctx = {'form': form, 'cf': 'FoodCreate'}
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
            ctx = {'form': form, 'cf': 'FoodCreate'}
            return render(request, self.template, ctx)
        fd = Food()
        user = request.user
        cafe = Cafe.objects.filter(Manager_id=user.id).first()
        count = Food.objects.filter(Cafe_id=cafe.id, Admin_Is_Active=True, Cafe__Manager_id=user.id).count()
        fd.Cafe = cafe
        fd.Image = form.cleaned_data['Image']
        fd.Title = form.cleaned_data['Title']
        cat_id = form.cleaned_data['FoodCategory']
        cat = FoodCategory.objects.filter(id=cat_id).first()
        fd.FoodCategory = cat
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
        fd.Gallery_Image_1 = form.cleaned_data['Gallery_Img_1']
        fd.Gallery_Image_2 = form.cleaned_data['Gallery_Img_2']
        fd.save()
        return redirect(self.success_url)


class FoodDetail(LoginRequiredMixin, View):
    template = 'adminpanel_food/food_detail_view.html'

    def get(self, request, pk):
        food = Food.objects.filter(id=pk, Admin_Is_Active=True).first()
        vpfd = '/' + food.Cafe.Cafe_UserName + "/" + "p" + "/" + str(food.id)
        vp = ViewOfPage.objects.filter(Page=vpfd).all().count()
        vpd = ViewOfPage.objects.filter(Page=vpfd, Time__day=datetime.datetime.now().day).all().count()
        vpy = ViewOfPage.objects.filter(Page=vpfd, Time__year=datetime.datetime.now().year).all().count()
        vpm = ViewOfPage.objects.filter(Page=vpfd, Time__month=datetime.datetime.now().month).all().count()
        ctx = {'food': food, 'vp': vp, 'vpd': vpd, 'vpy': vpy, 'vpm': vpm}
        return render(request, self.template, ctx)


class FoodUpdate(LoginRequiredMixin, View):
    success_url = reverse_lazy('food:all')
    template = 'adminpanel_food/food_form.html'

    def get(self, request, pk):
        fd = Food.objects.filter(pk=pk).first()
        form = FoodForm(initial={'Image': fd.Image, 'Is_Active': fd.Is_Active, })
        if fd.Gallery_Image_1 is not None:
            form.fields['Gallery_Img_1'].initial = fd.Gallery_Image_1
        if fd.Gallery_Image_2 is not None:
            form.fields['Gallery_Img_2'].initial = fd.Gallery_Image_2
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
        ctx = {'form': form, 'food': fd, 'cf': 'FoodUpdate'}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        fd = Food.objects.filter(id=pk).first()

        form = FoodForm(request.POST, request.FILES or None, initial={'Image': fd.Image, 'Is_Active': fd.Is_Active, })
        if fd.Gallery_Image_1 is not None:
            form.fields['Gallery_Img_1'].initial = fd.Gallery_Image_1
        if fd.Gallery_Image_2 is not None:
            form.fields['Gallery_Img_2'].initial = fd.Gallery_Image_2
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
            ctx = {'form': form, 'cf': 'FoodUpdate'}
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
        if not form.cleaned_data['Gallery_Img_1']:
            fd.Gallery_Image_1.delete()
        else:
            fd.Gallery_Image_1 = form.cleaned_data['Gallery_Img_1']

        if not form.cleaned_data['Gallery_Img_2']:
            fd.Gallery_Image_2.delete()
        else:
            fd.Gallery_Image_2 = form.cleaned_data['Gallery_Img_2']
        fd.save()
        return redirect(self.success_url)


@csrf_exempt
def save_data(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            json_data = json.loads(request.body)
            data = json_data['data']
            data = list(data)
            for item in data:
                food_id = str(item).split('_')[1]
                a_user = Food.objects.filter(Cafe__Manager_id=request.user.id, pk=food_id).first()
                if a_user is None:
                    return HttpResponse("error")
            temp = 1
            for item in data:
                food_id = str(item).split('_')[1]

                cafe = Cafe.objects.filter(Manager_id=request.user.id).first()
                f_food = Food.objects.filter(pk=food_id, Cafe_id=cafe.id, Admin_Is_Active=True,
                                             Cafe__Manager_id=request.user.id).first()
                f_food.First = temp
                temp = temp + 1
                f_food.save()

    return HttpResponse("save")


@csrf_exempt
def FoodDelete(request, *args, **kwargs):
    success_url = reverse_lazy('food:all')
    food_id = kwargs.get('pk')
    if food_id is not None:
        food = Food.objects.filter(pk=food_id, Cafe__Manager_id=request.user.id).delete()
        return redirect(success_url)
    raise Http404()
