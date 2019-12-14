from django.shortcuts import render
from .models import Meeting
from django.db.models import Count, Sum, Max, Min

app = 'reading'
def getHtml(html):
    return app+'/'+html+'.html'

def index(request):
    # list1 = Meeting.objects.order_by('date1','name')
    list1 = Meeting.objects.values('date1').annotate(headcnt=Count('name'))
   
    # list1 = Meeting.objects.values('club','club__name').annotate(meetingcnt=Count('date1',distinct=True),headcnt=Count('person',distinct=True)).order_by('club__name')
    
    context = {'list1': list1}
    # return render(request, 'case002/index.html', context)
    return render(request, getHtml('index'), context)

def date1(request,date1):
    key={'date1':date1}
    list1 = Meeting.objects.filter(date1=date1)
   
    # list1 = Meeting.objects.values('club','club__name').annotate(meetingcnt=Count('date1',distinct=True),headcnt=Count('person',distinct=True)).order_by('club__name')
    
    context = {'key': key,'list1': list1}
    # return render(request, 'case002/index.html', context)
    return render(request, getHtml('date1'), context)

def name(request,name):
    key={'name':name}
    list1 = Meeting.objects.filter(name=name)
   
    # list1 = Meeting.objects.values('club','club__name').annotate(meetingcnt=Count('date1',distinct=True),headcnt=Count('person',distinct=True)).order_by('club__name')
    
    context = {'key': key,'list1': list1}
    # return render(request, 'case002/index.html', context)
    return render(request, getHtml('name'), context)