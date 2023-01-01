import os
import uuid
from random import randint

from django.db import models
from dgmenu_cafe.models import Cafe
from dgmenu_food_category.models import FoodCategory

from io import BytesIO
from PIL import Image
from django.core.files import File


def compress(image):
    im = Image.open(image)
    im_io = BytesIO()
    size = (600, 500)
    im = im.resize(size, Image.ANTIALIAS)
    im.save(im_io, "PNG", optimize=True, quality=25, progressive=True)
    new_image = File(im_io, name=image.name)
    return new_image


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_name = randint(1, 100000)
    name, ext = get_filename_ext(filename)
    cafe_username = instance.Cafe.Cafe_UserName
    final_name = f"{uuid.uuid4().hex}{new_name}{ext}"
    return f"{cafe_username}/comestible/{final_name}"


def upload_image_gallery_path(instance, filename):
    new_name = randint(1, 100000)
    name, ext = get_filename_ext(filename)
    cafe_username = instance.Cafe.Cafe_UserName
    final_name = f"{uuid.uuid4().hex}{new_name}{ext}"
    return f"{cafe_username}/comestible/gallery/{final_name}"


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
    Admin_Is_Active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال مدیر')
    Is_Active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')
    Submit_Time = models.DateTimeField()
    Last_Edit_Time = models.DateTimeField()
    First = models.IntegerField(verbose_name='ترتیب نمایش')

    def save(self, *args, **kwargs):

        food = Food.objects.filter(id=self.id).first()
        if food is None:
            self.Image = compress(self.Image)
            if self.Gallery_Image_1 is not None:
                self.Gallery_Image_1 = compress(self.Gallery_Image_1)
            if self.Gallery_Image_2 is not None:
                self.Gallery_Image_2 = compress(self.Gallery_Image_2)
        else:
            if food.Image != self.Image:
                new_image = compress(self.Image)
            self.Image = new_image
            if food.Gallery_Image_1 != self.Gallery_Image_1:
                new_Gallery_Image_1 = compress(self.Gallery_Image_1)
            self.Gallery_Image_1 = new_Gallery_Image_1
            if food.Gallery_Image_2 != self.Gallery_Image_2:
                new_Gallery_Image_2 = compress(self.Gallery_Image_2)
            self.Gallery_Image_2 = new_Gallery_Image_2

        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'محصولات'
        verbose_name = 'محصول'

    def __str__(self):
        return self.Cafe.Cafe_UserName + "/" + self.Title
