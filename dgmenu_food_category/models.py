from django.db import models
from dgmenu_cafe.models import Cafe
import os
from random import randint


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_name = randint(1, 100000)
    name, ext = get_filename_ext(filename)
    final_name = f"{new_name}{ext}"
    return f"Cafe/category/img/{final_name}"


class FoodCategory(models.Model):
    Cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, verbose_name='کافه')
    NameFa = models.CharField(max_length=120, verbose_name='نام فارسی')
    NameEn = models.CharField(max_length=120, verbose_name='نام در ادرس')
    Img = models.ImageField(upload_to=upload_image_path, null=True, blank=True,
                            verbose_name='عکس')
    IsActive = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')
    IsActiveAdmin = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')
    First = models.IntegerField()
