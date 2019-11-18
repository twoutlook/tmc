from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TODO,Index
from .models import Note

from .models import AppPage
from .models import AppPageGrp,LogAppPage
from .models import SOP,SOPDetail

from .models import AppPage
from .models import AppPageMenu

from .models import AppPageAuthGrp

class AppPageAuthGrpResource(resources.ModelResource):
   class Meta:
        model = AppPageAuthGrp
class AppPageAuthGrpAdmin(ImportExportModelAdmin):
    resource_class = AppPageAuthGrpResource
    list_display = ('app','page','authgrp','is_active',)
    # list_filter = ['sop']
    # ordering = ('sop','seq')
    
    # search_fields = ['title',]
   
admin.site.register(AppPageAuthGrp, AppPageAuthGrpAdmin)




class AppPageMenuInline(admin.TabularInline):
    model = AppPageMenu
    extra = 1

class AppPageMenuResource(resources.ModelResource):
   class Meta:
        model = AppPageMenu
class AppPageMenuAdmin(ImportExportModelAdmin):
    resource_class = AppPageMenuResource
    list_display = ('id',)
    # list_filter = ['sop']
    # ordering = ('sop','seq')
    
    # search_fields = ['title',]
   
admin.site.register(AppPageMenu, AppPageMenuAdmin)


class SOPDetailInline(admin.TabularInline):
    model = SOPDetail
    extra = 1

class SOPResource(resources.ModelResource):
   class Meta:
        model = SOP
class SOPAdmin(ImportExportModelAdmin):
    resource_class = SOPResource
    inlines = [SOPDetailInline]
    list_display = ('name','note','is_active')
    list_filter = ['is_active',]
    # ordering = ('app','page')
    
    search_fields = ['note',]
   
admin.site.register(SOP, SOPAdmin)

class SOPDetailResource(resources.ModelResource):
   class Meta:
        model = SOPDetail
class SOPDetailAdmin(ImportExportModelAdmin):
    resource_class = SOPDetailResource
    list_display = ('sop','seq','title','note')
    list_filter = ['sop']
    ordering = ('sop','seq')
    
    search_fields = ['title',]
   
admin.site.register(SOPDetail, SOPDetailAdmin)


class AppPageGrpInline(admin.TabularInline):
    model = AppPageGrp
    extra = 1

class LogAppPageResource(resources.ModelResource):
   class Meta:
        model = LogAppPage
class LogAppPageAdmin(ImportExportModelAdmin):
    resource_class = LogAppPageResource
    # inlines = [AppPageGrpInline]
    list_display = ('app','page','ip','user','agent','data','stamp')
    list_filter = ['app','page','ip','user','data']
    # ordering = ('app','page')
    
    search_fields = ['agent',]
   
admin.site.register(LogAppPage, LogAppPageAdmin)
#    app = models.CharField(max_length=100)
#     page = models.CharField(max_length=100)
#     ip = models.CharField(max_length=100)
#     user = models.CharField(max_length=100)
#     agent = models.CharField(max_length=300)
#     stamp  = models.DateTimeField(default=timezone.now)
 


class AppPageResource(resources.ModelResource):
   class Meta:
        model = AppPage
class AppPageAdmin(ImportExportModelAdmin):
    resource_class = AppPageResource
    inlines = [AppPageGrpInline,AppPageMenuInline,]
    list_display = ('app','page','go_up','app_name','page_name','is_active')
    list_filter = ['app','page','title','is_active']
    ordering = ('app','page')
    
    search_fields = ['msg',]
   
admin.site.register(AppPage, AppPageAdmin)

class AppPageGrpResource(resources.ModelResource):
   class Meta:
        model = AppPageGrp
class AppPageGrpAdmin(ImportExportModelAdmin):
    resource_class = AppPageGrpResource
    list_display = ('apppage','grp')
    list_filter = ['apppage']
    ordering = ('apppage','grp')
    
    # search_fields = ['msg',]
   
admin.site.register(AppPageGrp, AppPageGrpAdmin)


class TODOResource(resources.ModelResource):
   class Meta:
        model = TODO
class TODOAdmin(ImportExportModelAdmin):
    resource_class = TODOResource
    list_display = ('title','brief','status','doer','detail','priority')
    list_filter = ['status',]
    # ordering = ('dept19','sub','seq',)
    ordering = ('-priority',)
    
    search_fields = ['title','brief',]
   

admin.site.register(TODO, TODOAdmin)


class NoteResource(resources.ModelResource):
   class Meta:
        model = Note
class NoteAdmin(ImportExportModelAdmin):
    resource_class = NoteResource
    list_display = ('grp','seq','title','note1','note2','note')
    list_filter = ['grp',]
    # ordering = ('dept19','sub','seq',)
    ordering = ('grp','seq')
    
    search_fields = ['title']
   

admin.site.register(Note, NoteAdmin)



class IndexResource(resources.ModelResource):
   class Meta:
        model = Index
class IndexAdmin(ImportExportModelAdmin):
    resource_class = IndexResource
    list_display = ('owner','app','seq','link','btn','disp','note','encoder','is_active')
    list_filter = ['owner','app','is_active']
    # ordering = ('dept19','sub','seq',)
    ordering = ('app','seq')
    # list_filter = ['app',]
    
    search_fields = ['disp',]
   

admin.site.register(Index, IndexAdmin)
