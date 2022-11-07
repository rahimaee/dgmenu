import uuid

from django.db import models
import os
from random import randint
from dgmenu_cafe.models import Cafe


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_name = randint(1, 100000)
    name, ext = get_filename_ext(filename)
    cafe_username = instance.Cafe.Cafe_UserName
    final_name = f"{uuid.uuid4().hex}{new_name}{ext}"
    return f"{cafe_username}/about/{final_name}"


class CafeAbout(models.Model):
    Title = models.CharField(max_length=250, verbose_name='عنوان معرفی')
    Description = models.CharField(max_length=500, verbose_name='متن معرفی')
    Image = models.ImageField(upload_to=upload_image_path, null=True, blank=True,
                              verbose_name='عکس')
    Cafe = models.ForeignKey(Cafe, verbose_name='کافه', on_delete=models.CASCADE)
