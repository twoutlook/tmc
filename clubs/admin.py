from django.contrib import admin

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# from .models import Data1
from .models import Meeting
from .models import Club
from .models import Person
from .models import Role



class RoleResource(resources.ModelResource):
    class Meta:
        model = Role

class RoleAdmin(ImportExportModelAdmin):
    resource_class = RoleResource
    list_display = ('name', 'fullname','id')   

admin.site.register(Role,RoleAdmin)




class ClubResource(resources.ModelResource):
    class Meta:
        model = Club

class ClubAdmin(ImportExportModelAdmin):
    resource_class = ClubResource
    list_display = ('name', 'fullname', 'id')   

admin.site.register(Club,ClubAdmin)


class PersonResource(resources.ModelResource):
    class Meta:
        model = Person

class PersonAdmin(ImportExportModelAdmin):
    resource_class = PersonResource
    list_display = ('club', 'name', 'fullname','is_member','member_since','note', 'id')   
    list_filter = ['club','is_member',]
    search_fields = ['name','fullname']
  
admin.site.register(Person,PersonAdmin)


class MeetingResource(resources.ModelResource):
    class Meta:
        model = Meeting

class MeetingAdmin(ImportExportModelAdmin):
    resource_class = MeetingResource
    list_display = ('club','date1', 'person','role2')
    fields = ('club','date1', 'person', 'role2')
    list_filter = ['club','person','role2']
    search_fields = ['date1']
   
admin.site.register(Meeting,MeetingAdmin)

