from django.db import models
from dgmenu_account.models import CustomUser as MyUser
from dgmenu_cafe.models import Cafe as cafe


# Create your models here.


class Role(models.Model):
    Name = models.CharField(max_length=150, verbose_name='نام دسترسی')
    Cafe = models.ForeignKey(cafe, on_delete=models.CASCADE, verbose_name='نام کافه')
    User = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='کابر')
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
