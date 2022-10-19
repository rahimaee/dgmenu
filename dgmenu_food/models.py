import os
from random import randint

from django.db import models
from dgmenu_cafe.models import Cafe
from dgmenu_food_category.models import FoodCategory


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_name = randint(1, 100000)
    name, ext = get_filename_ext(filename)
    final_name = f"{new_name}{ext}"
    return f"comestible/{final_name}"


def upload_image_gallery_path(instance, filename):
    new_name = randint(1, 100000)
    name, ext = get_filename_ext(filename)
    final_name = f"{new_name}{ext}"
    return f"comestible/gallery/{final_name}"


# Create your models here.
class Food(models.Model):
    Cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, verbose_name='کافه')
    Image = models.ImageField(default='avatar.png', upload_to=upload_image_path, verbose_name='عکس اصلی غذا')
    Title = models.CharField(max_length=200, null=False, verbose_name='نام')
    Description_Short = models.CharField(max_length=250, verbose_name='توضیح کوتاه')
    Description_Long = models.CharField(max_length=500, verbose_name='توضیح زیاد')
    FoodCategory = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, verbose_name='دسته بندی', blank=True,
                                     null=True)
    Ingredients = models.CharField(max_length=250, verbose_name='مواد تشکیل دهنده')
    Calories = models.CharField(max_length=50, verbose_name='کالری')
    Tag = models.CharField(max_length=250, verbose_name='برچسب ها')
    Allergy = models.CharField(max_length=250, verbose_name='الرژی')
    Price = models.CharField(max_length=100, verbose_name='قیمت')
    Discount = models.CharField(max_length=200, null=True, blank=True, verbose_name='قیمت باتخفیف')
    Gallery_Image_1 = models.ImageField(default='avatar.png', upload_to=upload_image_path, verbose_name='عکس اصلی غذا')
    Gallery_Image_2 = models.ImageField(default='avatar.png', upload_to=upload_image_path, verbose_name='عکس اصلی غذا')
    Gallery_Image_3 = models.ImageField(default='avatar.png', upload_to=upload_image_path, verbose_name='عکس اصلی غذا')
    Admin_Is_Active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال مدیر')
    Is_Active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')
    Submit_Time = models.DateTimeField()
    Last_Edit_Time = models.DateTimeField()
    First = models.IntegerField(verbose_name='ترتیب نمایش')



