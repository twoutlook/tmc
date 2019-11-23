from django.contrib import admin

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# from .models import Data1
from .models import Meeting
from .models import Club
from .models import Person
from .models import Role

# from .models import PersonClub
from .models import ClubDate


from .models import Data2
from .models import Best



# class Data1Resource(resources.ModelResource):
#     class Meta:
#         model = Data1

# class Data1Admin(ImportExportModelAdmin):
#     resource_class = Data1Resource
#     list_display = ('date1','place', 'worker','thing')
#     list_filter = ['place','worker']
#     search_fields = ['date1','thing']
   
# admin.site.register(Data1, Data1Admin)

class ClubDateResource(resources.ModelResource):
    class Meta:
        model = ClubDate

class ClubDateAdmin(ImportExportModelAdmin):
    resource_class = ClubDateResource
    list_display = ('date1', 'club', 'note')   

admin.site.register(ClubDate,ClubDateAdmin)

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


class Data2Resource(resources.ModelResource):
    class Meta:
        model = Data2

class Data2Admin(ImportExportModelAdmin):
    resource_class = Data2Resource
    list_display = ('date1','name', 'member','role')
    fields = ('date1','name', 'member','role')
    list_filter = ['name','role','member']
    search_fields = ['date1']
   
admin.site.register(Data2, Data2Admin)

class BestResource(resources.ModelResource):
    class Meta:
        model = Best

class BestAdmin(ImportExportModelAdmin):
    resource_class = BestResource
    list_display = ('date1','title','name')
    list_filter = ['title','name',]
    search_fields = ['date1']
   
admin.site.register(Best, BestAdmin)