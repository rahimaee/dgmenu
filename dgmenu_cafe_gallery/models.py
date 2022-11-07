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
    return f"{cafe_username}/gallery/{final_name}"


# Create your models here.

class CafeGallery(models.Model):
    Name = models.CharField(max_length=120, verbose_name='نام عکس')
    Img = models.ImageField(upload_to=upload_image_path, null=True, blank=True,
                            verbose_name='عکس')
    IsActiveAdmin = models.BooleanField(default=True, verbose_name='فعال/غیرفعال مدیر')
    TimeUpload = models.DateTimeField(verbose_name='زمان ثبت عکس')
    Cafe = models.ForeignKey(Cafe, verbose_name='کافه', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "گالری تصاویر"
        verbose_name = "تصویر"

    def __str__(self):
        return self.Cafe.Cafe_UserName + str(self.id) + self.Name
