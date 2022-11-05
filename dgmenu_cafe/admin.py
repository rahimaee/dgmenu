from django.contrib import admin
from .models import Cafe


# Register your models here.

class CafeAdmin(admin.ModelAdmin):
    search_fields = ['Cafe_UserName']


admin.site.register(Cafe, CafeAdmin)
