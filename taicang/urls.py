
from django.contrib import admin
from django.urls import path,include 
from django.views.generic import TemplateView

from . import views

app_name = 'taicang'

urlpatterns = [
    # path('about/', TemplateView.as_view(template_name="reading/about.html")),
    # path('date/<date1>/', views.date1, name='date1'),
    path('sum1/', views.sum1, name='sum1'),
    path('get_name/', views.get_name, name='get_name'),
    path('input_phone/', views.input_phone, name='input_phone'),
    path('input_phone/phone_result/', views.phone_result, name='phone_result'),
    path('', views.index, name='index'),
  
]
# https://wsvincent.com/django-image-uploads/
# if settings.DEBUG: # new
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)