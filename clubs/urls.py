from django.urls import path
from . import views
from django.views.generic import TemplateView
app_name = 'clubs'

urlpatterns = [
    
    path('person_list/', views.person_list, name='person_list'),
    path('person_list/<int:club>/', views.person_list_club, name='person_list_club'),
    path('person_list/<int:club>/<int:person>/', views.person_list_club_person, name='person_list_club_person'),
    path('person_list/<int:club>/<int:person>/edit/', views.edit_person, name='edit_person'),
    path('person_list/<int:club_id>/add/', views.add_person, name='add_person'),


    # https://simpleisbetterthancomplex.com/tutorial/2018/01/29/how-to-implement-dependent-or-chained-dropdown-list-with-django.html
    #path('ajax/load-persons/', views.load_persons, name='ajax_load_persons'),  # <-- this one here
    
   
    path('add_meeting/', views.add_meeting, name='add_meeting'),
    path('meeting_detail/<int:pk>/', views.meeting_detail, name='meeting_detail'),
    # path('<int:club>/', views.club, name='club'),
    # path('<int:club_id>/add_meeting/', views.club_add_meeting, name='club_add_meeting'),
    path('<int:club_id>/meeting/<int:pk>/', views.club_meeting_detail, name='club_meeting_detail'),
    path('<int:club>/person/', views.club_person_list, name='club_person_list'),
    path('<int:club>/person/<int:person>/', views.club_person, name='club_person'),
    path('<int:club>/member/', views.club_member_list, name='club_member_list'),
    path('<int:club>/member/start/', views.club_member_list_start, name='club_member_list_start'),
    path('<int:club>/member/start/email/', views.club_member_list_start_email, name='club_member_list_start_email'),
    path('<int:club>/member/start/team/<team>/', views.club_member_list_start_team, name='club_member_list_start_team'),
    path('<int:club_id>/member/start/team/<team>/<int:person_id>/edit/', views.club_member_list_start_team_edit, name='club_member_list_start_team_edit'),
    # path('<int:club_id>/member/start/team/<team>/<int:person_id>/del/', views.club_member_list_start_team_del, name='club_member_list_start_team_del'),
    path('<int:club_id>/member/start/<int:person_id>/edit/', views.club_member_list_start_edit, name='club_member_list_start_edit'),
    path('<int:club>/member/start/<membertype>/', views.club_member_list_start_membertype, name='club_member_list_start_membertype'),
    path('<int:club>/member/<int:person_id>/', views.club_member, name='club_member'),
    path('<int:club>/guest/', views.club_guest_list, name='club_guest_list'),
    path('<int:club>/guest/<int:person_id>/', views.club_guest, name='club_guest'),
    
    path('<int:club_id>/meeting/', views.club_meeting_list, name='club_meeting_list'),
    path('<int:club_id>/meeting/add/', views.club_add_meeting, name='club_add_meeting'),
    path('<int:club_id>/meeting/<date1>/', views.club_meeting, name='club_meeting'),
    path('<int:club_id>/meeting/<date1>/add/', views.club_add_meeting_with_date, name='club_add_meeting_with_date'),
    path('<int:club_id>/meeting/<date1>/<person_id>/<role_id>/del/', views.club_meeting_del, name='club_meeting_del'),
    path('<int:club_id>/meeting/<date1>/<person_id>/<role_id>/del/confirm/', views.club_meeting_del_confirm, name='club_meeting_del_confirm'),
    path('<int:club>/meeting/<date1>/role/', views.club_date_role, name='club_date_role'),
    # path('<int:club>/<date1>/', views.club_date, name='club_date'),
    # path('<int:club>/<date1>/role/', views.club_date_role, name='club_date_role'),
    path('', views.index, name='index'),
    path('testing1210', views.testing1210, name='testing1210'),

    # path('huadao/', TemplateView.as_view(template_name="huadao/index.html")),
    path('vision/', TemplateView.as_view(template_name="vision/vision.html")),
    path('vision/member/', TemplateView.as_view(template_name="vision/member.html")),
    path('vision/saa/', TemplateView.as_view(template_name="vision/saa.html")),
]