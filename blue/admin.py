
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Task
# from .models import Market

# task_id = models.IntegerField(unique=True)
#     event_id = models.IntegerField()
#     department= models.CharField(max_length=32,default='---')
#     work_no = models.IntegerField()
#     work_name= models.CharField(max_length=32,default='---')
#     status= models.CharField(max_length=32,default='---')
    
#     start_time = models.DateTimeField(blank=True,null=True)
#     end_time = models.DateTimeField(,blank=True,null=True)
#     description= models.CharField(max_length=100,blank=True,null=True)
#     reason= models.CharField(max_length=100,blank=True,null=True)
#     improvement= models.CharField(max_length=100,blank=True,null=True)
#     deal_type= models.CharField(max_length=32,blank=True,null=True)
  

class TaskResource(resources.ModelResource):
    class Meta:
        model = Task

class TaskAdmin(ImportExportModelAdmin):
    resource_class = TaskResource
    list_display = ('event_id', 'department', 'work_no', 'work_name', 'status','description', 'deal_type')   
    list_filter = ('department', 'work_name', 'status', 'deal_type')
    search_fields = ['description']
admin.site.register(Task,TaskAdmin)

