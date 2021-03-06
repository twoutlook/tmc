# https://docs.djangoproject.com/en/2.2/_modules/django/contrib/auth/hashers/#make_password
import django.contrib.auth.hashers

from django.shortcuts import render,get_object_or_404
from django.db.models import Count, Sum, Max, Min
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
import re
from django.contrib.auth.decorators import login_required

from .models import Meeting
from .models import Club

from .models import Person
from .models import Role
from django.http import HttpResponseRedirect

from .models import Best
from .forms import MeetingForm
from .forms import PersonStartForm
from .forms import PersonStartNoteForm


from .forms import ClubMeetingForm
from .forms import ClubMeetingWithDateForm


# https://simpleisbetterthancomplex.com/tutorial/2018/01/29/how-to-implement-dependent-or-chained-dropdown-list-with-django.html
from .forms import MeetingFormV2 

from .forms import PersonForm

from django.shortcuts import redirect
# https://pypi.org/project/django-pivot/
from django_pivot.pivot import pivot
from django_pivot.histogram import histogram

# testing1210
# https://stackoverflow.com/questions/12921789/django-import-auth-user-to-the-model
from django.contrib.auth.models import User

app = 'clubs'
def getHtml(html):
    return app+'/'+html+'.html'

class PersonListView(ListView):
    model = Person
    # paginate_by = 20
    context_object_name = 'people'

class PersonCreateView(CreateView):
    model = Person
    # fields = ('name', 'birthdate', 'country', 'city')
    form_class = PersonForm
    success_url = reverse_lazy('xxxperson_changelist')



def person_list(request):
    # club = Club.objects.get(id=club)
    key={'club':None}
    list1 = Person.objects.order_by('club__name','name')
   
    # list1 = Meeting.objects.values('club','club__name').annotate(meetingcnt=Count('date1',distinct=True),headcnt=Count('person',distinct=True)).order_by('club__name')
    
    context = {'key': key,'list1': list1}
    # return render(request, 'case002/index.html', context)
    return render(request, getHtml('person_list_v2'), context)

def person_list_club(request,club):
    club = Club.objects.get(id=club)
    key={'club':club}
    list1 = Person.objects.filter(club=club,is_member=True)
    list2 = Person.objects.filter(club=club,is_member=False)
   
    # list1 = Meeting.objects.values('club','club__name').annotate(meetingcnt=Count('date1',distinct=True),headcnt=Count('person',distinct=True)).order_by('club__name')
    
    context = {'key': key,'list1': list1,'list2': list2}
    # return render(request, 'case002/index.html', context)
    return render(request, getHtml('person_list_club'), context)



def person_list_club_person(request,club,person):
    club = Club.objects.get(id=club)
    person = Person.objects.get(id=person)
    # person = get_object_or_404(Person, pk=person)
    # club = get_object_or_404(Club, pk=club)
  
    key={'club':club,'person':person}
    # list1 = Person.objects.filter(club=club,id=person)
   
    # list1 = Meeting.objects.values('club','club__name').annotate(meetingcnt=Count('date1',distinct=True),headcnt=Count('person',distinct=True)).order_by('club__name')
    
    context = {'key': key,'x': person}
    # return render(request, 'case002/index.html', context)
    return render(request, getHtml('person_list_club_person'), context)

def index(request):
    list1 = Club.objects.order_by('name')
   
    # list1 = Meeting.objects.values('club','club__name').annotate(meetingcnt=Count('date1',distinct=True),headcnt=Count('person',distinct=True)).order_by('club__name')
    
    context = {'list1': list1}
    # return render(request, 'case002/index.html', context)
    return render(request, getHtml('index'), context)


def club(request,club):
    club = Club.objects.get(id = club)
    
    key={'club':club}

    # obj = Club.objects.get(id = club)
    list1 = Meeting.objects.filter(club=club).values('date1').annotate(headcnt=Count('person',distinct=True))
    # key={'obj':obj}

    # pivot_table = pivot(list1, 'date1', 'member', 'id',aggregation=Count)
    # for x in pivot_table:
    #     x['total']=x['Member']+x['Guest']
  
    context = {'key': key,'list1': list1}
    return render(request,getHtml('club') , context)

def club_meeting_list(request,club_id):
    club = Club.objects.get(id = club_id)
    
    key={'club':club}

    list1 = Meeting.objects.filter(club=club).values('date1').annotate(headcnt=Count('person',distinct=True),reccnt=Count('id'))
   
    context = {'key': key,'list1': list1}
    return render(request,getHtml('club_meeting_list') , context)


def add_person(request,club_id):
    club = Club.objects.get(id=club_id)
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.club =club
            post.save()
            return redirect('../'+str(post.pk)+"/")
            # context = {'obj': post}
    
            # return render(request,getHtml('meeting_detail/'+str(post.pk)+'/') , context)


        else:
            # pass
            print('POST but not valid...')
            # form = MeetingForm()
            context = {'form': form}
            return render(request,getHtml('add_person') , context)

    else:
        # pass
        form = PersonForm()
        context = {'club': club,'form': form}
        return render(request,getHtml('add_person') , context)

def edit_person(request,club,person):
    club = get_object_or_404(Club, pk=club)
    person = post = get_object_or_404(Person, pk=person)
    key={'club':club,'person':person,}
    if request.method == "POST":
        form = PersonForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.club = club
            # post.created_date = timezone.now()
            post.save()
            # return redirect('post_detail', pk=post.pk)
            return HttpResponseRedirect("../")
        else:
            print(' NOT valid')
           
    else:
        form = PersonForm(instance=post)
    
    return render(request, getHtml('edit_person'), {'form': form,'key': key})

# https://simpleisbetterthancomplex.com/tutorial/2018/01/29/how-to-implement-dependent-or-chained-dropdown-list-with-django.html
def load_persons(request):
    country_id = request.GET.get('club')
    persons = Person.objects.filter(club_id=country_id).order_by('name')
    # persons = Person.objects.order_by('name')
    
    return render(request, 'clubs/person_dropdown_list_options.html', {'persons': persons})

@login_required(login_url='/admin/login/?next=/')
def club_add_meeting(request,club_id):
    club = Club.objects.get(id=club_id)
    key={'club':club}
    msg = None

    if  request.user.groups.filter(name = 'west_add_meeting').exists():
        print("current user HAS group 'west_add_meeting'")

    else:
        form = ClubMeetingForm()
        
        print("current user doesn't have group 'west_add_meeting'")
        msg ="Current account is Not allowed to add meeting of club "+ club.name
        context = {'form': form,'key':key,'msg':msg}
           
        return render(request,getHtml('club_add_meeting') , context)
            

    if request.method == 'POST':
        form = ClubMeetingForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False)
            
            post.club = club

            print("going to use ",post.persontxt, " to get obj")
            persons = Person.objects.filter(club=club_id,name=post.persontxt)

            if persons.count() != 1:
                print(" Not found this obj, or logic wrong with more than one objs")
                
                msg ="Person not found"
                list1 =Person.objects.filter(club=club_id).order_by('name')
                temp = '<br>'
                for x in list1:
                    temp += x.name+ '<br>'
                msg += temp
                context = {'form': form,'key':key,'msg':msg}
           
                return render(request,getHtml('club_add_meeting') , context)
            
            # Already
            meetings = Meeting.objects.filter(club=club_id,date1=post.date1,person=persons[0],role2=post.role2)
            if meetings.count() == 1:
                print(" Not found this obj, or logic wrong with more than one objs")
                msg ="Club|Date|Person|Role exists!"
                context = {'form': form,'key':key,'msg':msg}
           
                return render(request,getHtml('club_add_meeting') , context)
            

            post.person = persons[0]
            post.save()
            return redirect('../')
            # context = {'obj': post}
    
            # return render(request,getHtml('meeting_detail/'+str(post.pk)+'/') , context)


        else:
            # pass
            print('POST but not valid...')
            # form = MeetingForm()
            # context = {'form': form,'key':key}
            # return render(request,getHtml('club_add_meeting') , context)

    else:
        # pass
        form = ClubMeetingForm()
        # context = {'form': form}
    
    # NOTE: for NOT POST, and also for POST not valid
    context = {'form': form,'key':key}
           
    return render(request,getHtml('club_add_meeting') , context)


@login_required(login_url='/admin/login/?next=/')
def club_meeting_del_confirm(request,club_id,date1,person_id,role_id):
    club = Club.objects.get(id=club_id)
    meeting = Meeting.objects.get(club=club_id, date1=date1, person = person_id, role2= role_id)
    key={'club':club,'obj':meeting,}
    print("... going to add meeting : ", meeting.__dict__)
    msg = None

    if  request.user.groups.filter(name = 'west_add_meeting').exists():
        print("current user HAS group 'west_add_meeting'")
        context = {'key':key,'msg':msg}
           
        # return render(request,getHtml('club_meeting_del') , context)
        meeting.delete()
        return redirect('../../../../')
           
      
    else:
        
        print("current user doesn't have group 'west_add_meeting'")
        msg ="Current account is Not allowed to Del meeting of club "+ club.name
        context = {'key':key,'msg':msg}
           
        return render(request,getHtml('club_meeting_del') , context)
            

@login_required(login_url='/admin/login/?next=/')
def club_meeting_del(request,club_id,date1,person_id,role_id):
    club = Club.objects.get(id=club_id)
    meeting = Meeting.objects.get(club=club_id, date1=date1, person = person_id, role2= role_id)
    key={'club':club,'obj':meeting,}
    print("... going to add meeting : ", meeting.__dict__)
    msg = None

    if  request.user.groups.filter(name = 'west_add_meeting').exists():
        print("current user HAS group 'west_add_meeting'")
        context = {'key':key,'msg':msg}
           
        return render(request,getHtml('club_meeting_del') , context)
      
    else:
        
        print("current user doesn't have group 'west_add_meeting'")
        msg ="Current account is Not allowed to Del meeting of club "+ club.name
        context = {'key':key,'msg':msg}
           
        return render(request,getHtml('club_meeting_del') , context)
            

    if request.method == 'POST':
        form = ClubMeetingForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False)
            
            post.club = club

            print("going to use ",post.persontxt, " to get obj")
            persons = Person.objects.filter(club=club_id,name=post.persontxt)

            if persons.count() != 1:
                print(" Not found this obj, or logic wrong with more than one objs")
                
                msg ="Person not found"
                list1 =Person.objects.filter(club=club_id).order_by('name')
                temp = '<br>'
                for x in list1:
                    temp += x.name+ '<br>'
                msg += temp
                context = {'form': form,'key':key,'msg':msg}
           
                return render(request,getHtml('club_add_meeting') , context)
            
            # Already
            meetings = Meeting.objects.filter(club=club_id,date1=post.date1,person=persons[0],role2=post.role2)
            if meetings.count() == 1:
                print(" Not found this obj, or logic wrong with more than one objs")
                msg ="Club|Date|Person|Role exists!"
                context = {'form': form,'key':key,'msg':msg}
           
                return render(request,getHtml('club_add_meeting') , context)
            

            post.person = persons[0]
            post.save()
            return redirect('../')
            # context = {'obj': post}
    
            # return render(request,getHtml('meeting_detail/'+str(post.pk)+'/') , context)


        else:
            # pass
            print('POST but not valid...')
            # form = MeetingForm()
            # context = {'form': form,'key':key}
            # return render(request,getHtml('club_add_meeting') , context)

    else:
        # pass
        form = ClubMeetingForm()
        # context = {'form': form}
    
    # NOTE: for NOT POST, and also for POST not valid
    context = {'form': form,'key':key}
           
    return render(request,getHtml('club_add_meeting') , context)



@login_required(login_url='/admin/login/?next=/')
def club_member_list_start_edit(request,club_id,person_id):
    club = Club.objects.get(id=club_id)
    person = Person.objects.get(id=person_id)
    
    key={'club':club,'person':person}
    msg = None

    if  request.user.groups.filter(name = 'west_add_meeting').exists():
        print("current user HAS group 'west_add_meeting'")

    else:
        form = PersonStartForm()
        
        print("current user doesn't have group 'west_add_meeting'")
        msg ="Current account is Not allowed to add meeting of club "+ club.name
        context = {'form': form,'key':key,'msg':msg}
           
        return render(request,getHtml('club_member_list_start_edit') , context)
            
    post = get_object_or_404(Person, pk=person_id)
  
    if request.method == 'POST':
        form = PersonStartForm(request.POST, instance=post)
        
        if form.is_valid():
            post = form.save(commit=False)
            
            post.save()
            return redirect('../../')
            # context = {'obj': post}
    
            # return render(request,getHtml('meeting_detail/'+str(post.pk)+'/') , context)


        else:
            # pass
            print('POST but not valid...')
            # form = MeetingForm()
            # context = {'form': form,'key':key}
            # return render(request,getHtml('club_add_meeting') , context)

    else:
        # pass
        form = PersonStartForm( instance=post)
        
        # form = ClubMeetingForm()
        # context = {'form': form}
    
    # NOTE: for NOT POST, and also for POST not valid
    context = {'form': form,'key':key}
           
    return render(request,getHtml('club_member_list_start_edit') , context)


@login_required(login_url='/admin/login/?next=/')
def club_member_list_start_team_edit(request,club_id,team,person_id):
    club = Club.objects.get(id=club_id)
    person = Person.objects.get(id=person_id)
    
    key={'club':club,'person':person}
    msg = None

    if  request.user.groups.filter(name = 'west_add_meeting').exists():
        print("current user HAS group 'west_add_meeting'")

    else:
        form = PersonStartNoteForm()
        
        print("current user doesn't have group 'west_add_meeting'")
        msg ="Current account is Not allowed to add meeting of club "+ club.name
        context = {'form': form,'key':key,'msg':msg}
           
        return render(request,getHtml('club_member_list_start_note_edit') , context)
            
    post = get_object_or_404(Person, pk=person_id)
  
    if request.method == 'POST':
        form = PersonStartNoteForm(request.POST, instance=post)
        
        if form.is_valid():
            post = form.save(commit=False)
            
            post.save()
            return redirect('../../')
            # context = {'obj': post}
    
            # return render(request,getHtml('meeting_detail/'+str(post.pk)+'/') , context)


        else:
            # pass
            print('POST but not valid...')
            # form = MeetingForm()
            # context = {'form': form,'key':key}
            # return render(request,getHtml('club_add_meeting') , context)

    else:
        # pass
        form = PersonStartNoteForm( instance=post)
        
        # form = ClubMeetingForm()
        # context = {'form': form}
    
    # NOTE: for NOT POST, and also for POST not valid
    context = {'form': form,'key':key}
           
    return render(request,getHtml('club_member_list_start_note_edit') , context)



@login_required(login_url='/admin/login/?next=/')
def club_add_meeting_with_date(request,club_id,date1):
    club = Club.objects.get(id=club_id)
    key={'club':club,'date1':date1}
    msg = None

    if  request.user.groups.filter(name = 'west_add_meeting').exists():
        print("current user HAS group 'club_add_meeting_with_date'")

    else:
        form = ClubMeetingWithDateForm()
        
        print("current user doesn't have group 'west_add_meeting'")
        msg ="Current account is Not allowed to add meeting of club "+ club.name
        context = {'form': form,'key':key,'msg':msg}
           
        return render(request,getHtml('club_add_meeting_with_date') , context)
            

    if request.method == 'POST':
        form = ClubMeetingWithDateForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False)
            
            post.club = club
            post.date1 = date1

            print("going to use ",post.persontxt, " to get obj")
            persons = Person.objects.filter(club=club_id,name=post.persontxt)

            if persons.count() != 1:
                print(" Not found this obj, or logic wrong with more than one objs")
                
                msg ="Person not found! Possible name as follows: "
                list1 =Person.objects.filter(club=club_id).order_by('name')
                temp = '<br>'
                for x in list1:
                    temp += " "+x.name+ ','
                msg += temp[0:-1]
                context = {'form': form,'key':key,'msg':msg}
           
                return render(request,getHtml('club_add_meeting_with_date') , context)
            
            # Already
            meetings = Meeting.objects.filter(club=club_id,date1=date1,person=persons[0],role2=post.role2)
            if meetings.count() == 1:
                print(" Not found this obj, or logic wrong with more than one objs")
                msg ="Club|Date|Person|Role exists!"
                context = {'form': form,'key':key,'msg':msg}
           
                return render(request,getHtml('club_add_meeting_with_date') , context)
            

            post.person = persons[0]
            post.save()
            return redirect('../')
            # context = {'obj': post}
    
            # return render(request,getHtml('meeting_detail/'+str(post.pk)+'/') , context)


        else:
            # pass
            print('POST but not valid...')
            # form = MeetingForm()
            # context = {'form': form,'key':key}
            # return render(request,getHtml('club_add_meeting') , context)

    else:
        # pass
        form = ClubMeetingWithDateForm()
        # context = {'form': form}
    
    # NOTE: for NOT POST, and also for POST not valid
    context = {'form': form,'key':key}
           
    return render(request,getHtml('club_add_meeting_with_date') , context)



def add_meeting(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/meeting_detail/'+str(post.pk)+"/")
            # context = {'obj': post}
    
            # return render(request,getHtml('meeting_detail/'+str(post.pk)+'/') , context)


        else:
            # pass
            print('POST but not valid...')
            # form = MeetingForm()
            context = {'form': form}
            return render(request,getHtml('add_meeting') , context)

    else:
        # pass
        form = MeetingForm()
        context = {'form': form}
        return render(request,getHtml('add_meeting') , context)


def meeting_detail(request,pk):
    obj = Meeting.objects.get(pk=pk)
    

    # pivot_table = pivot(list1, 'date1', 'member', 'id',aggregation=Count)
    # for x in pivot_table:
    #     x['total']=x['Member']+x['Guest']
  
    context = {'obj': obj}
    return render(request,getHtml('meeting_detail') , context)

def testing1210(request):
    list1 = User.objects.all()
    members = Person.objects.filter(club__name = 'West', is_member = True)
    print (" to list West member as follows, ")
    cnt = 0
    for x in members:
        cnt += 1
        print(cnt,x.name,x.phone)

        list2 = User.objects.filter(username=x.phone)
        if list2:
            obj =list2[0]
            obj.is_staff = True
        # https://docs.djangoproject.com/en/2.2/topics/auth/passwords/
        # obj.password='xxx'

        # https://www.laurivan.com/change-a-django-password-manually/
            obj.set_password(x.phone)
            obj.save()

        else: # Not yet created
            obj = User(username=x.phone,first_name=x.name)
            obj.is_staff = True
            obj.set_password(x.phone)
            obj.save()

            # print (list2[0], ' was created!')
            

    # obj = User(username='123',first_name='user123')
    # try:
    #     obj.save()
    # except Exception as e:
    #     print("nicely ...",e)
    #     obj = User.objects.get(username='123')
    #     obj.first_name ='aaa'
    #     obj.is_staff = True
    #     # https://www.laurivan.com/change-a-django-password-manually/
    #     obj.set_password('123')
    #     obj.save()
    

    context = {'list1': list1}
    return render(request,getHtml('testing1210') , context)



def club_meeting_detail(request,club_id,pk):
    obj = Meeting.objects.get(pk=pk)
    context = {'obj': obj}
    return render(request,getHtml('club_meeting_detail') , context)





def club_date(request,club,date1):
    list1 = Meeting.objects.filter(club=club,date1=date1).values('person','person__name').annotate(rolecnt=Count('id')).order_by('person__name')
    club = Club.objects.get(id = club)
    
    key={'club':club,'date1':date1}

    for x in list1:
        person = x['person']
        list2 = Meeting.objects.filter(club=club,date1=date1,person=person)
        # roles =''
        # for x2 in list2:
        #     roles += "["+x2.role2.name+"] "
        x['roles']= list2
    # pivot_table = pivot(list1, 'date1', 'member', 'id',aggregation=Count)
    # for x in pivot_table:
    #     x['total']=x['Member']+x['Guest']
  
    context = {'list1': list1,'key':key}
    return render(request,getHtml('club_date') , context)

def club_meeting(request,club_id,date1):
    list1 = Meeting.objects.filter(club=club_id,date1=date1).values('person','person__name','person__is_member').annotate(rolecnt=Count('id')).order_by('person__name')
    club = Club.objects.get(id = club_id)
    
    key={'club':club,'date1':date1}

    for x in list1:
        person = x['person']
        list2 = Meeting.objects.filter(club=club,date1=date1,person=person)
        # roles =''
        # for x2 in list2:
        #     roles += "["+x2.role2.name+"] "
        x['roles']= list2
        x['act']='del'
    # pivot_table = pivot(list1, 'date1', 'member', 'id',aggregation=Count)
    # for x in pivot_table:
    #     x['total']=x['Member']+x['Guest']
  
    context = {'list1': list1,'key':key}
    return render(request,getHtml('club_meeting') , context)


def club_meeting_role(request,club,date1):
    list1 = Meeting.objects.filter(club=club,date1=date1).values('role2','role2__name').annotate(rolecnt=Count('id')).order_by('role2__name')
    club = Club.objects.get(id = club)
    
    key={'club':club,'date1':date1}

    for x in list1:
        role2 = x['role2']
        list2 = Meeting.objects.filter(club=club,date1=date1,role2=role2)
        # roles =''
        # for x2 in list2:
        #     roles += "["+x2.role2.name+"] "
        x['names']= list2
    # pivot_table = pivot(list1, 'date1', 'member', 'id',aggregation=Count)
    # for x in pivot_table:
    #     x['total']=x['Member']+x['Guest']
  
    context = {'list1': list1,'key':key}
    return render(request,getHtml('club_meeting_role') , context)

def club_date_role(request,club,date1):
    list1 = Meeting.objects.filter(club=club,date1=date1).values('role2','role2__name').annotate(rolecnt=Count('id')).order_by('role2__name')
    club = Club.objects.get(id = club)
    
    key={'club':club,'date1':date1}

    for x in list1:
        role2 = x['role2']
        list2 = Meeting.objects.filter(club=club,date1=date1,role2=role2)
        # roles =''
        # for x2 in list2:
        #     roles += "["+x2.role2.name+"] "
        x['names']= list2
    # pivot_table = pivot(list1, 'date1', 'member', 'id',aggregation=Count)
    # for x in pivot_table:
    #     x['total']=x['Member']+x['Guest']
  
    context = {'list1': list1,'key':key}
    return render(request,getHtml('club_date_role') , context)


def xxxclub_person_list(request,club):
    # list1 = Meeting.objects.filter(club=club).values('person','person__name').annotate(meetingcnt=Count('date1',distinct=True)).order_by('-meetingcnt','person__name')
    list1 = Person.objects.filter(club=club).order_by('name')
    
    club = Club.objects.get(id = club)
    # for x in list1:
        # person = x['person']
        # profile = Person.objects.get(id=x['person'])
        # x['profile']=profile
    
    key={'club':club}

    
    context = {'list1': list1,'key':key}
    return render(request,getHtml('club_person_list') , context)

def club_person_list(request,club):
    club = Club.objects.get(id=club)
    key={'club':club}
    list1 = Person.objects.filter(club=club,is_member=True)
    list2 = Person.objects.filter(club=club,is_member=False)
   
    # list1 = Meeting.objects.values('club','club__name').annotate(meetingcnt=Count('date1',distinct=True),headcnt=Count('person',distinct=True)).order_by('club__name')
    
    context = {'key': key,'list1': list1,'list2': list2}
    # return render(request, 'case002/index.html', context)
    return render(request, getHtml('club_person_list'), context)

def club_member_guest_list(request,club,is_member):
    club = Club.objects.get(id=club)
    key={'club':club,'is_member':is_member,}
    list1 = Person.objects.filter(club=club,is_member=is_member)
    # list2 = Person.objects.filter(club=club,is_member=False)
   
    # list1 = Meeting.objects.values('club','club__name').annotate(meetingcnt=Count('date1',distinct=True),headcnt=Count('person',distinct=True)).order_by('club__name')
    
    context = {'key': key,'list1': list1}
    # return render(request, 'case002/index.html', context)
    return render(request, getHtml('club_member_guest_list'), context)

@login_required(login_url='/admin/login/?next=/')   
def club_member_list_start(request,club):
    club = Club.objects.get(id=club)
    key={'club':club,}
    list1 = Person.objects.filter(club=club,is_member=True)
    # list2 = Person.objects.filter(club=club,is_member=False)
   
    # list1 = Meeting.objects.values('club','club__name').annotate(meetingcnt=Count('date1',distinct=True),headcnt=Count('person',distinct=True)).order_by('club__name')
    
    context = {'key': key,'list1': list1}
    # return render(request, 'case002/index.html', context)
    return render(request, getHtml('club_member_list_start'), context)

@login_required(login_url='/admin/login/?next=/')   
def club_member_list_start_email(request,club):
    club = Club.objects.get(id=club)
    key={'club':club,}
    list1 = Person.objects.filter(club=club,is_member=True)
    # list2 = Person.objects.filter(club=club,is_member=False)
   
    # list1 = Meeting.objects.values('club','club__name').annotate(meetingcnt=Count('date1',distinct=True),headcnt=Count('person',distinct=True)).order_by('club__name')
    
    context = {'key': key,'list1': list1}
    # return render(request, 'case002/index.html', context)
    return render(request, getHtml('club_member_list_start_email'), context)

@login_required(login_url='/admin/login/?next=/')   
def club_member_list_start_membertype(request,club,membertype):
    club = Club.objects.get(id=club)
    key={'club':club,'membertype':membertype,}
    list1 = Person.objects.filter(club=club,is_member=True,member_type=membertype)
    # list2 = Person.objects.filter(club=club,is_member=False)
   
    # list1 = Meeting.objects.values('club','club__name').annotate(meetingcnt=Count('date1',distinct=True),headcnt=Count('person',distinct=True)).order_by('club__name')
    
    context = {'key': key,'list1': list1}
    # return render(request, 'case002/index.html', context)
    return render(request, getHtml('club_member_list_start'), context)

@login_required(login_url='/admin/login/?next=/')   
def club_member_list_start_team(request,club,team):
    club = Club.objects.get(id=club)
    key={'club':club,'team':team}
    list1 = Person.objects.filter(club=club,is_member=True,teamleader=team)
    # list2 = Person.objects.filter(club=club,is_member=False)
   
    # list1 = Meeting.objects.values('club','club__name').annotate(meetingcnt=Count('date1',distinct=True),headcnt=Count('person',distinct=True)).order_by('club__name')
    
    context = {'key': key,'list1': list1}
    # return render(request, 'case002/index.html', context)
    return render(request, getHtml('club_member_list_start_team'), context)



def club_member_list(request,club):
    return club_member_guest_list(request,club,True)
    
def club_guest_list(request,club):
    return club_member_guest_list(request,club,False)
    
    

def club_member(request,club,person_id):
    return club_member_guest(request,club,person_id,True)

def club_guest(request,club,person_id):
    return club_member_guest(request,club,person_id,False)

def club_member_guest(request,club,person_id,is_member):
    # person = Person.objects.get(id=person)
    person = get_object_or_404(Person, pk=person_id)
    club = get_object_or_404(Club, pk=club)
    
    # print(person.__dict__)
    list1 = Meeting.objects.filter(club=club,person=person).values('date1').annotate(rolecnt=Count('role2'))
    # club = Club.objects.get(id = club)
    
    for x in list1:
        date1 = x['date1']
        list2 = Meeting.objects.filter(club=club,person=person,date1=date1)
        # roles =''
        # for x2 in list2:
        #     roles += "["+x2.role2.name+"] "
        x['role2s']= list2
    


    key={'club':club,'person':person,}

    
    context = {'list1': list1,'key':key}
    return render(request,getHtml('club_member_guest') , context)


def club_person(request,club,person):
    # person = Person.objects.get(id=person)
    person = get_object_or_404(Person, pk=person)
    club = get_object_or_404(Club, pk=club)
    
    # print(person.__dict__)
    list1 = Meeting.objects.filter(club=club,person=person).values('date1').annotate(rolecnt=Count('role2'))
    # club = Club.objects.get(id = club)
    
    for x in list1:
        date1 = x['date1']
        list2 = Meeting.objects.filter(club=club,person=person,date1=date1)
        # roles =''
        # for x2 in list2:
        #     roles += "["+x2.role2.name+"] "
        x['role2s']= list2
    


    key={'club':club,'person':person,}

    
    context = {'list1': list1,'key':key}
    return render(request,getHtml('club_person') , context)

