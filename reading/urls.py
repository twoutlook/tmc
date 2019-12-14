
from django.contrib import admin
from django.urls import path,include 
from django.views.generic import TemplateView

from . import views

app_name = 'reading'

urlpatterns = [
    path('about/', TemplateView.as_view(template_name="reading/about.html")),
    path('date/<date1>/', views.date1, name='date1'),
    path('name/<name>/', views.name, name='name'),
    path('', views.index, name='index'),
  
]
# https://wsvincent.com/django-image-uploads/
# if settings.DEBUG: # new
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)