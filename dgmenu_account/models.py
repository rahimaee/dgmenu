import os
import uuid
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
    return f"profile/{uuid.uuid4().hex}{final_name}"


class CustomUser(AbstractUser):
    Profile = models.ImageField(default='avatar.png', upload_to=upload_image_path, verbose_name='پروفایل')
    PhoneNumber = models.CharField(max_length=100, blank=True, null=True, verbose_name='موبایل')
    PhoneNumber_confirm = models.BooleanField(default=False, blank=True, verbose_name='تایید حساب کاربری')
    Gender = models.CharField(max_length=10, blank=True, null=True, verbose_name='جنسیت')

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"


class Role(models.Model):
    Name = models.CharField(max_length=150, verbose_name='نام دسترسی')
    # درباره ما
    Cafe_About_edit = models.BooleanField(default=False, verbose_name='ویرایش درباره ما')
    # تتظیمات
    Cafe_settings_edit = models.BooleanField(default=False, verbose_name='تنظیمات کافه')
    # دسته بندی
    Cafe_category_view = models.BooleanField(default=False, verbose_name='مشاهده دسته بندی')
    Cafe_category_edit = models.BooleanField(default=False, verbose_name='ویرایش دسته بندی')
    Cafe_category_add = models.BooleanField(default=False, verbose_name='اضافه کردن دسته بندی')
    Cafe_category_delete = models.BooleanField(default=False, verbose_name='حذف کردن دسته بندی')
    # محصول
    Cafe_food_view = models.BooleanField(default=False, verbose_name='مشاهده محصول')
    Cafe_food_edit = models.BooleanField(default=False, verbose_name='ویرایش محصول')
    Cafe_food_add = models.BooleanField(default=False, verbose_name='اضافه کردن محصول')
    Cafe_food_delete = models.BooleanField(default=False, verbose_name='حذف کردن محصول')

    # گالری

    Cafe_gallery_view = models.BooleanField(default=False, verbose_name='مشاهده گالری')
    Cafe_gallery_edit = models.BooleanField(default=False, verbose_name='ویرایش گالری')
    Cafe_gallery_add = models.BooleanField(default=False, verbose_name='اضافه کردن گالری')
    Cafe_gallery_delete = models.BooleanField(default=False, verbose_name='حذف کردن گالری')
    # تیم
    Cafe_team_view = models.BooleanField(default=False, verbose_name='مشاهده تیم')
    Cafe_team_edit = models.BooleanField(default=False, verbose_name='ویرایش تیم')
    Cafe_team_add = models.BooleanField(default=False, verbose_name='اضافه کردن تیم')
    Cafe_team_delete = models.BooleanField(default=False, verbose_name='حذف کردن تیم')
