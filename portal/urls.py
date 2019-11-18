from django.urls import path
from django.views.generic import TemplateView
from . import views
app_name = 'portal'

# https://docs.djangoproject.com/en/2.2/topics/class-based-views/
urlpatterns = [
    # path('auth', views.auth, name='auth'),
   
    # path('permission/', views.mark, name='mark'),
    path('', views.index, name='index'),
   
    # path('', TemplateView.as_view(template_name="portal/index.html")),
    path('about/', TemplateView.as_view(template_name="portal/about.html")),
    # path('vs001/', TemplateView.as_view(template_name="portal/vs001.html")),
]