# from django.contrib import admin
# from .models import FoodCategory
#
# # Register your models here.
# admin.site.register(FoodCategory)
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import FoodCategory

admin.site.register(FoodCategory, MPTTModelAdmin)
