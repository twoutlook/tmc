from django.shortcuts import render

from datetime import date, timedelta
from datetime import datetime

from .models import Note
from .models import Wk

def index(request):
    list = Note.objects.all()
    context = {'list': list}
    return render(request, 'note/index.html', context)

def ww(request):
    list = Wk.objects.all()
    context = {'list': list}
    return render(request, 'note/ww.html', context)

def init_ww(request):
    def getList():
        return Wk.objects.order_by('yr','num')
    def getCnt():
        return Wk.objects.count()

def ww2(request):
    def getList():
        return Wk.objects.order_by('yr','num')
    def getCnt():
        return Wk.objects.count()
        
    # https://docs.djangoproject.com/en/2.2/intro/tutorial02/
    # list = Wk.objects.order_by('yr','num')
    list = getList()
    
    for x in list:
        x.delete()
 
    k1 = getCnt()
    
    d1='2018-12-31'
    date1 = datetime.strptime(d1, "%Y-%m-%d")
    date2 =date1 + timedelta(days=6)
   
    for num in range(1,53):
        # print(num) # to ensure num is 1,2,3 ..., 52
        date2 =date1 + timedelta(days=6)
        
        x =Wk(yr=2019,num=num,date1=date1,date2=date2)
        x.save()
        
        date1 =date2 + timedelta(days=1)
        
    k2 = getCnt()
    
    user = request.user

    key={'k1':k1,'k2':k2}
    list = getList()
    context = {'user': user,'key': key,'list':list }
    return render(request, 'note/ww2.html', context)