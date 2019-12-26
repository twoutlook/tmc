
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Flower
from .models import Market


class FlowerResource(resources.ModelResource):
    class Meta:
        model = Flower

class FlowerAdmin(ImportExportModelAdmin):
    resource_class = FlowerResource
    list_display = ('name', 'group')   

admin.site.register(Flower,FlowerAdmin)


class MarketResource(resources.ModelResource):
    class Meta:
        model = Market

class MarketAdmin(ImportExportModelAdmin):
    resource_class = MarketResource
    list_display = ('dt', 'flower','p1','p2')   

admin.site.register(Market,MarketAdmin)


