from django.shortcuts import render,get_object_or_404
from django.db.models import Count, Sum, Max, Min
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
import re

from .models import Meeting
from .models import Club

from .models import Person
from .models import Role
from django.http import HttpResponseRedirect

from .models import Best
from .forms import MeetingForm
from .forms import PersonForm

from django.shortcuts import redirect
# https://pypi.org/project/django-pivot/
from django_pivot.pivot import pivot
from django_pivot.histogram import histogram

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


def rolecnt(request):
    list1 = Data2.objects.exclude(role='---').exclude(role='Absence').values('date1').annotate(headcnt=Count('role',distinct=True))
    

    # pivot_table = pivot(list1, 'date1', 'member', 'id',aggregation=Count)
    # for x in pivot_table:
    #     x['total']=x['Member']+x['Guest']
  
    context = {'list1': list1}
    return render(request,getHtml('rolecnt') , context)
def rolecnt_date(request,date1):
    list1 = Data2.objects.exclude(role='---').exclude(role='Absence').filter(date1=date1).values('role').annotate(rolecnt=Count('id')).order_by('role')
    key={'date1':date1}

    for x in list1:
        role = x['role']
        list2 = Data2.objects.exclude(role='---').exclude(role='Absence').filter(date1=date1,role=role)
        names =''
        for x2 in list2:
            # print(x2.name)
            names += "["+x2.name+"] "
        x['names']= names
    # pivot_table = pivot(list1, 'date1', 'member', 'id',aggregation=Count)
    # for x in pivot_table:
    #     x['total']=x['Member']+x['Guest']
  
    context = {'list1': list1,'key':key}
    return render(request,getHtml('rolecnt_date') , context)



def headcnt_date(request,date1):
    list1 = Data2.objects.exclude(role='---').exclude(role='Absence').filter(date1=date1).values('name','member').annotate(rolecnt=Count('id')).order_by('name')
    key={'date1':date1}

    for x in list1:
        name = x['name']
        list2 = Data2.objects.exclude(role='---').exclude(role='Absence').filter(date1=date1,name=name)
        roles =''
        for x2 in list2:
            # print(x2.role)
            roles += "["+x2.role+"] "
        x['roles']= roles
    # pivot_table = pivot(list1, 'date1', 'member', 'id',aggregation=Count)
    # for x in pivot_table:
    #     x['total']=x['Member']+x['Guest']
  
    context = {'list1': list1,'key':key}
    return render(request,getHtml('headcnt_date') , context)


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

def club_person_list(request,club):
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

def s1_date(request,date1):
    list1 = Data2.objects.exclude(role='---').exclude(role='Absence').filter(date1=date1).values('date1','member').annotate(headcnt=Count('id'))
    list2 = Data2.objects.exclude(role='---').exclude(role='Absence').filter(date1=date1).order_by('-member','name')
    
    pivot_table = pivot(list1, 'date1', 'member', 'id',aggregation=Count)
    for x in pivot_table:
        try:
    #your code
            x['total']=x['Member']+x['Guest']
        
        except Exception as ex:
            # print(ex)
            x['total']=x['Member']
        # print(x)
   
            
        # print(x)
    context = {'list1': pivot_table,'list2':list2}
    return render(request, getHtml('s1_date'), context)

def s2(request):
    list1 = Data2.objects.exclude(role='---').exclude(role='Absence').values('name').annotate(pointssum=Sum('points')).filter(pointssum__gt = 0).order_by('-pointssum')
    context = {'list1': list1}
    return render(request, getHtml('s2'), context)

def s2_name(request,name):
    list1 = Data2.objects.exclude(role='---').exclude(role='Absence').filter(name=name).order_by('date1')
    context = {'list1': list1,'name': name}
    return render(request, getHtml('s2_name'), context)

def s3(request):
    list1 = Data2.objects.filter(role__in = ['Ah-counter','GE','Grammarian','TME','TT Evaluator','TT-master','Timer'])
    pivot_table = pivot(list1, 'date1', 'role', 'name',aggregation=Min)
    for x in pivot_table:
        x['Ah']=x['Ah-counter']
        x['TT_Evaluator']=x['TT Evaluator']
        x['TT_master']=x['TT-master']
        # print(x)
    context = {'list1': pivot_table}
    return render(request, getHtml('s3'), context)

def best(request):
    pivot_table = pivot(Best, 'date1', 'title', 'name',aggregation=Min)
    # for x in pivot_table:
        # print(x)
    context = {'list1': pivot_table}
    return render(request,getHtml('best'), context)


def s4(request):
    list1 = Data2.objects.filter(role__in = ['Speaker','IE']).values('date1').annotate(cnt=Count('id')).order_by('date1')
    # list1 = Data2.objects.filter(role__in = ['Speaker','IE']).order_by('date1','-role','name')
    for x in list1:
        list2 = Data2.objects.filter(date1= x['date1'],role = 'Speaker')
        list3 = Data2.objects.filter(date1= x['date1'],role = 'IE')
        speaker = ''
        ie = ''

        def getNameStr(listx):
            speaker = ''
            cnt = 0
            for x2 in listx:
                cnt += 1
                speaker = speaker +"("+str(cnt)+")"+ x2.name+" "
            return speaker

        # cnt = 0
        # for x2 in list2:
        #     cnt += 1
        #     speaker = speaker +"("+str(cnt)+")"+ x2.name+" "

        x['speaker']=getNameStr(list2)
        x['ie']=getNameStr(list3)

        # cnt = 0
        # for x3 in list3:
        #     cnt += 1
        #     ie = ie +"("+str(cnt)+")"+ x3.name+" "

        # x['ie']=ie
    
    
        # print(x)
    context = {'list1': list1}
    return render(request, getHtml('s4'),  context)
