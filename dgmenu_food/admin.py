from django.contrib import admin
from .models import Food, Gallery


class FoodGalleryInline(admin.StackedInline):
    model = Gallery


class FoodAdmin(admin.ModelAdmin):
    inlines = [FoodGalleryInline]


# Register your models here.
admin.site.register(Food, FoodAdmin)
