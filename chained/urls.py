from django.urls import include, path

from . import views

urlpatterns = [
    # path('', views.PersonListView.as_view(), name='person_changelist'),
    path('', views.person_changelist, name='person_changelist'),
    path('add/', views.PersonCreateView.as_view(), name='person_add'),
    # path('/', views.PersonUpdateView.as_view(), name='person_change'),
]