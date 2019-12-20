from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# from .models import Data1
from .models import Ticket



class TicketResource(resources.ModelResource):
    class Meta:
        model = Ticket

class TicketAdmin(ImportExportModelAdmin):
    resource_class = TicketResource
    list_display = ('seq','name', 'phone','clubtxt','club','note','feetxt','stattxt','dt')   

admin.site.register(Ticket,TicketAdmin)

#   seq = models.IntegerField(default = 0)
#     name = models.CharField(max_length=32)
#     phone = models.CharField(max_length=11)
#     clubtxt = models.CharField(max_length=100)
#     note = models.CharField(max_length=100)
#     feetxt = models.CharField(max_length=100)
#     stattxt = models.CharField(max_length=100)
#     dt = models.DateTimeField()