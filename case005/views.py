from django.shortcuts import render
from django.db.models import Count, Sum, Max, Min
import re
from .models import Data2
from .models import Meeting
from .models import Club

from .models import Person
from .models import Role


from .models import Best


# https://pypi.org/project/django-pivot/
from django_pivot.pivot import pivot
from django_pivot.histogram import histogram

app = 'case005'
def getHtml(html):
    return app+'/'+html+'.html'

def index(request):
    list1 = Meeting.objects.values('club','club__name').annotate(meetingcnt=Count('date1',distinct=True),headcnt=Count('person',distinct=True)).order_by('club__name')
    
    context = {'list1': list1}
    # return render(request, 'case002/index.html', context)
    return render(request, getHtml('index'), context)

def init0(request):
    list1 = Data2.objects.order_by('date1','name')
    cnt = 0 
    for x in list1:
        # print(x.__dict__)
        cnt += 1
        print(cnt, x.date1,x.name,x.role)
        club = Club.objects.get(name='West')
        person = Person.objects.get(name='---')
        role = Role.objects.get(name='---')
        
        Meeting(club=club,person=person,role2=role,name=x.name,date1=x.date1,role=x.role).save()
            
    context = {'list1': list}
    # return render(request, 'case002/index.html', context)
    return render(request, getHtml('init1'), context)


def init1(request):
    list1 = Meeting.objects.order_by('date1','name')
    for x in list1:
        print(x.club,x.date1,x.name,x.person)
        if x.person.name == '---':
            print('...going to add name', x.name)
            
            person_list = Person.objects.filter(name = x.name)
            if person_list:
                person = person_list[0]
            else:
                person = Person(name=x.name,fullname=x.name)
            
                # print(person.__dict__)
                person.save()
            x.person = person
            x.save()
            print("after auto fill ",x.club,x.date1,x.name,x.person)

        if x.role2.name == '---':
            print('...going to update role2 ')
            
            role_list = Role.objects.filter(name = x.role)
            if role_list:
                role = role_list[0]
            else:
                
                print("ERR HERE ...")
            x.role2 = role
            x.save()
            print("after role2 ",x.club,x.date1,x.name,x.person)
            
    context = {'list1': list}
    # return render(request, 'case002/index.html', context)
    return render(request, getHtml('init1'), context)


def s1(request):
    list1 = Data2.objects.exclude(role='---').exclude(role='Absence').values('date1','member').annotate(headcnt=Count('id'))
    
    pivot_table = pivot(list1, 'date1', 'member', 'id',aggregation=Count)
    for x in pivot_table:
        x['total']=x['Member']+x['Guest']
        # print(x)
    context = {'list1': pivot_table}
    return render(request,getHtml('s1') , context)

def headcnt(request):
    list1 = Data2.objects.exclude(role='---').exclude(role='Absence').values('date1').annotate(headcnt=Count('name',distinct=True))
    

    # pivot_table = pivot(list1, 'date1', 'member', 'id',aggregation=Count)
    # for x in pivot_table:
    #     x['total']=x['Member']+x['Guest']
  
    context = {'list1': list1}
    return render(request,getHtml('headcnt') , context)


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
    list1 = Meeting.objects.filter(club=club).values('person','person__name').annotate(meetingcnt=Count('date1',distinct=True)).order_by('-meetingcnt','person__name')
    club = Club.objects.get(id = club)
    for x in list1:
        # person = x['person']
        profile = Person.objects.get(id=x['person'])
        x['profile']=profile
    
    key={'club':club}

    
    context = {'list1': list1,'key':key}
    return render(request,getHtml('club_person_list') , context)

def club_person(request,club,person):
    person = Person.objects.get(id=person)
    list1 = Meeting.objects.filter(club=club,person=person).values('date1').annotate(rolecnt=Count('role2'))
    club = Club.objects.get(id = club)
    
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
