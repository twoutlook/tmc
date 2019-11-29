from django.contrib import admin

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# from .models import Data1
from .models import Country
from .models import City
from .models import Person



class CountryResource(resources.ModelResource):
    class Meta:
        model = Country

class CountryAdmin(ImportExportModelAdmin):
    resource_class = CountryResource
    list_display = ('name',)
    # list_filter = ['place','worker']
    # search_fields = ['date1','thing']
   
admin.site.register(Country, CountryAdmin)

class CityResource(resources.ModelResource):
    class Meta:
        model = City

class CityAdmin(ImportExportModelAdmin):
    resource_class = CityResource
    list_display = ('name','country')
    # list_filter = ['place','worker']
    # search_fields = ['date1','thing']
   
admin.site.register(City, CityAdmin)

class PersonResource(resources.ModelResource):
    class Meta:
        model = Person

class PersonAdmin(ImportExportModelAdmin):
    resource_class = PersonResource
    # birthdate
    list_display = ('name','birthdate','country','city')
    # list_filter = ['place','worker']
    # search_fields = ['date1','thing']
   
admin.site.register(Person, PersonAdmin)
