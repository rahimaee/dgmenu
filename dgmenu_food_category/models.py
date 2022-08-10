from django.db import models
from dgmenu_cafe.models import Cafe
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.

class FoodCategory(models.Model):
    Cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, verbose_name='برای کافه/رستوران')
    Name_Fa = models.CharField(max_length=120, verbose_name='نام فارسی', unique=True)
    Name_En = models.CharField(max_length=120, verbose_name='نام انگلیسی')
    Icon = models.CharField(max_length=150, verbose_name='نام ایکون')
    Parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = u'Categoría'
        verbose_name_plural = u'Categorias'

    class MPTTMeta:
        order_insertion_by = ['Name_Fa']

    def __unicode__(self):
        return self.name
