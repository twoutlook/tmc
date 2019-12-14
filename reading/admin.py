from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# from .models import Data1
from .models import Meeting



class MeetingResource(resources.ModelResource):
    class Meta:
        model = Meeting

class MeetingAdmin(ImportExportModelAdmin):
    resource_class = MeetingResource
    list_display = ('date1','name', 'note')   

admin.site.register(Meeting,MeetingAdmin)
