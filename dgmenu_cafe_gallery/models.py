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
    final_name = f"{new_name}{ext}"
    return f"Cafe/gallery/{final_name}"


# Create your models here.

class CafeGallery(models.Model):
    Name = models.CharField(max_length=120, verbose_name='نام عکس')
    Img = models.ImageField(upload_to=upload_image_path, null=True, blank=True,
                            verbose_name='عکس')
    IsActiveAdmin = models.BooleanField(default=True, verbose_name='فعال/غیرفعال مدیر')
    TimeUpload = models.DateTimeField(verbose_name='زمان ثبت عکس')
    Cafe = models.ForeignKey(Cafe, verbose_name='کافه', on_delete=models.CASCADE)
