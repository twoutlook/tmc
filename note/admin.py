
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Note, Note002


# NOTE： WW project
from .models import Wk
class WkResource(resources.ModelResource):
    class Meta:
        model = Wk

class WkAdmin(ImportExportModelAdmin):
    resource_class = WkResource
    # inlines = [BuyFoodDetInline,CookedInline]
    list_display = ('yr','num', 'date1','date2')
    list_filter = ['yr']
    # search_fields = ['date1','data']
   
admin.site.register(Wk, WkAdmin)