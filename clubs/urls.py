from django.urls import path
from . import views
app_name = 'clubs'

urlpatterns = [
    # path('person_changelist/', views.PersonListView.as_view(), name='person_changelist'),
    path('person_list/', views.person_list, name='person_list'),
    # path('person_changelist/<int:club>/', views.person_list_club, name='person_list_club'),
    path('person_list/<int:club>/', views.person_list_club, name='person_list_club'),
    # path('person_changelist/<int:club>/<int:person>/', views.person_list_club_person, name='person_list_club_person'),
    path('person_list/<int:club>/<int:person>/', views.person_list_club_person, name='person_list_club_person'),
    path('person_list/<int:club>/<int:person>/edit/', views.edit_person, name='edit_person'),
    # path('person_changelist/<int:club>/add/', views.PersonCreateView.as_view(), name='person_add'),
    # path('person_changelist/<int:club>/add_person/', views.add_person, name='add_person'),
    path('person_list/<int:club_id>/add/', views.add_person, name='add_person'),


    # https://simpleisbetterthancomplex.com/tutorial/2018/01/29/how-to-implement-dependent-or-chained-dropdown-list-with-django.html
    path('ajax/load-persons/', views.load_persons, name='ajax_load_persons'),  # <-- this one here
    
    # path('add/', views.PersonCreateView.as_view(), name='person_add'),
    # path('<int:pk>/', views.PersonUpdateView.as_view(), name='person_change'),
    # path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'), 

    path('add_meeting/', views.add_meeting, name='add_meeting'),
    path('meeting_detail/<int:pk>/', views.meeting_detail, name='meeting_detail'),
    path('<int:club>/', views.club, name='club'),
    path('<int:club_id>/add_meeting/', views.club_add_meeting, name='club_add_meeting'),
    path('<int:club_id>/meeting/<int:pk>/', views.club_meeting_detail, name='club_meeting_detail'),
    path('<int:club>/person/', views.club_person_list, name='club_person_list'),
    path('<int:club>/person/<int:person>/', views.club_person, name='club_person'),
    path('<int:club>/<date1>/', views.club_date, name='club_date'),
    path('<int:club>/<date1>/role/', views.club_date_role, name='club_date_role'),
    path('', views.index, name='index'),
]