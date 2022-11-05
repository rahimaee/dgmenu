from django.contrib import admin
from .models import Food


class FoodAdmin(admin.ModelAdmin):
    list_display = ('Cafe', 'id', 'Title')
    search_fields = ['Title__icontains', 'Cafe__Cafe_UserName__icontains', ]


admin.site.register(Food, FoodAdmin)
