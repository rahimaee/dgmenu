import uuid

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
    cafe_username = instance.Cafe.Cafe_UserName
    final_name = f"{uuid.uuid4().hex}{new_name}{ext}"
    return f"{cafe_username}/category/img/{final_name}"


class FoodCategory(models.Model):
    Cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, verbose_name='کافه')
    NameFa = models.CharField(max_length=120, verbose_name='نام فارسی')
    NameEn = models.CharField(max_length=120, verbose_name='نام در ادرس')
    Img = models.ImageField(upload_to=upload_image_path, null=True, blank=True,
                            verbose_name='عکس')
    IsActive = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')
    IsActiveAdmin = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')
    First = models.IntegerField()

    class Meta:
        verbose_name_plural = "دسته بندی"
        verbose_name = "دسته"

    def __str__(self):
        return self.Cafe.Cafe_UserName + str(self.id) + self.NameFa
