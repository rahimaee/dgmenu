import os
from random import randint

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_name = randint(1, 100000)
    name, ext = get_filename_ext(filename)
    final_name = f"{new_name}{ext}"
    return f"profile/{final_name}"


class CustomUser(AbstractUser):
    PhoneNumber = models.CharField(max_length=100, verbose_name='موبایل')
    profile = models.ImageField(default='avatar.png', upload_to=upload_image_path, verbose_name='پروفایل')
    PhoneNumber_confirm = models.BooleanField(default=False, verbose_name='تایید حساب کاربری')

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"
