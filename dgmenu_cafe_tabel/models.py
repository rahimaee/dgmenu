import os
from random import randint

from django.db import models
from dgmenu_cafe.models import Cafe
import uuid


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_name = randint(1, 100000)
    name, ext = get_filename_ext(filename)
    cafe_username = instance.Cafe.Cafe_UserName
    final_name = f"{uuid.uuid4().hex}{new_name}{ext}"
    return f"{cafe_username}/tabel/{final_name}"


class CafeTabel(models.Model):
    Name = models.CharField(max_length=120, verbose_name='نام میز')
    Cafe = models.ForeignKey(Cafe, verbose_name='کافه', on_delete=models.CASCADE)
    IsActive = models.BooleanField(default=True, verbose_name='فعال/غیرفعال', null=True)
    IsActiveAdmin = models.BooleanField(default=True, verbose_name='فعال/غیرفعال مدیر', null=True)
    UnId = models.CharField(default="hamayarmenu", max_length=250, verbose_name='ایدی بیرونی', null=True)
    Img = models.ImageField(default='avatar.png', upload_to=upload_image_path, verbose_name='عکس میز')

