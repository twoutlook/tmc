from django.urls import path
from django.views.generic import TemplateView
from . import views
app_name = 'blog'

# https://docs.djangoproject.com/en/2.2/topics/class-based-views/
urlpatterns = [
    # path('auth', views.auth, name='auth'),
   
    # path('permission/', views.mark, name='mark'),
    # path('', views.index, name='index'),
   
    # path('', TemplateView.as_view(template_name="portal/index.html")),
    # path('about/', TemplateView.as_view(template_name="portal/about.html")),
    path('launch/', TemplateView.as_view(template_name="blog/launch.html")),
    path('event1222/', TemplateView.as_view(template_name="blog/event1222.html")),
    path('2019-12-19/', TemplateView.as_view(template_name="blog/2019-12-19.html")),
    path('2019-12-20/', TemplateView.as_view(template_name="blog/2019-12-20.html")),
    # path('vs001/', TemplateView.as_view(template_name="portal/vs001.html")),
]