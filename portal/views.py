from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from django.http import HttpResponse
from django.http import HttpResponseRedirect


import xlsxwriter
import os
from django.utils import timezone
import time

from django.shortcuts import render
from django.db.models import Count,Sum
# https://stackoverflow.com/questions/739776/how-do-i-do-an-or-filter-in-a-django-query
# Item.objects.filter(Q(creator=owner) | Q(moderated=False))
from django.db.models import Q

# https://docs.djangoproject.com/en/2.2/topics/auth/default/
from django.contrib.auth.decorators import login_required
# /admin/login/?next=/

from django.db.models.functions import TruncMonth, TruncYear


from portal.models import Index
from portal.models import AppPage
from portal.models import SOP,SOPDetail


from .forms import NameForm
from .forms import PartForm

from .models import AppPageAuthGrp
from .models import Note


app_name ='portal'
app_dir = 'portal/'
def get_html(val):
    return app_dir+val
def get_portal_html(val):
    return 'portal/'+val+'.html'

def get_template_no_user_app_page():
    return 'portal/no_user_app_page.html'

# NOTE:
# 2019-09-17
# 這是目前覺得封裝比較好的
# 回傳 結果，模板，內容
# 讓調用者運用
# 使用範例
# from portal.views import get_user_app_page_status
#
# status,template,context=get_user_app_page_status(request.user,'fin','fa')
#     if status == False:
#         return render(request, template, context)
#
# -------------------------
# 1. 在 portal::AppPageAuthGrp 維護

    # app 
    # page 
    # authgrp
    # 這是軟性應對到 Authentication and Authorization administration
    # 的 Groups
    # 命名規則
    # g-fin 一般財務權限，做為前台頁面訪問的控制，不開通任何後台權限
    # grp-fin 做為後台增刪改查

    # 再由 Users 的指定用戶加入上述的 g-
  
# -------------------------

def get_user_app_page_status(user,app,page):
    context={'user':user,'app':app,'page':page}
    checking =  is_user_app_page(user,app,page) 
    template = get_template_no_user_app_page()
    return checking,template,context


def get_html_by_def(val):
    return app_name+'/'+val+'.html'

def is_user_in_group(user,group):
    # if user.is_superuser:
    #     return True
    return user.groups.filter(name=group).exists()

#
# 用戶的所有群組是否合乎指定的 app:page
# NOTE: 2019-09-17
# 在 AppPageAuthGrp 的 authgrp 欄位
# 允許以逗號分隔多個權限組
def is_user_app_page(user,app,page):
    # print("is_user_app_page...")
    # print("1. identify current user is ",user)
    # print("2. having groups ",user.groups)
    # for x in user.groups.all():
    #     print('zzz',x)

    # print("3. auth groups of given app page ",app,page)

    if not AppPageAuthGrp.objects.filter(app=app,page=page).exists():
        # 啟用 is_user_app_page
        # 但沒有維護必要的 authgrp
        # 視同
        # print("no profile of ", app, page)
        return False
    auth = AppPageAuthGrp.objects.get(app=app,page=page)
    
    # print("DEBUG...auth is ",auth)
    
    authArr =auth.authgrp.split(',')

    # print("DEBUG...authArr is ",authArr)
    for x in authArr:
        # print ('required... >>>'+x+"<<<")
        # print ('required... >>>'+x.strip()+"<<<")
   
        for y in user.groups.all():
            # print(x.strip(), 'is in ',y)
            x = x.strip()

            # print("DEBUG... loop  user.groups.all()  ",y)
            # NOTE: str(y) is a must!
            if x == str(y):
            # if x == y:
                print(" YES! to return")
                return True

    # print("auth is ", auth.authgrp)
    
    return False



def is_user_in_groups(user,groups):
    # if user.is_superuser:
    #     return True
    for group in groups:
        if user.groups.filter(name=group).exists():
            return True
    return False



def get_page(app,page):
    page_list = AppPage.objects.filter(app=app,page=page)
    if page_list.count() != 1:
        return None
    return page_list[0]
   

def index_template(request,app,app_name,go_up,page_name):
    list = Index.objects.filter(app=app,is_active=True).order_by('seq')
    user = request.user
    context = {'app_name': app_name,'go_up': go_up,'page_name': page_name,'list': list,'user':user}
    return render(request, 'portal/index_template.html', context)
def index_template_top(request,app,app_name,go_up,page_name):
    list = Index.objects.filter(app=app,is_active=True).order_by('seq')
    user = request.user
    context = {'app_name': app_name,'go_up': go_up,'page_name': page_name,'list': list,'user':user}
    return render(request, 'portal/index_template_top.html', context)




@login_required(login_url='/admin/login/?next=/')
def index(request):
    # app ={'app':'portal','disp':'信息系統入口','note':'頂層目錄'}
    app ='portal'
    app_name = 'Case003信息系統入口'
    go_up =''
    page_name='信息系統頂層目錄'
    # list = Index.objects.filter(app='portal').filter(is_active=True).order_by('seq')
    # user = request.user
    # context = {'app': app,'list': list,'user':user}
    return index_template_top(request,app,app_name,go_up,page_name)

# @login_required(login_url='/admin/login/?next=/')
# def index(request):
#     app ={'app':'portal','disp':'信息系統入口','note':'頂層目錄'}
#     list = Index.objects.filter(app='portal').filter(is_active=True).order_by('seq')
#     user = request.user
#     context = {'app': app,'list': list,'user':user}
#     return render(request, get_html('app_index.html'), context)



@login_required(login_url='/admin/login/?next=/')
def sop(request):
    # app ={'app':'portal','disp':'信息系統入口','note':'頂層目錄'}
    # app['note']='頂層目錄'
    list = SOP.objects.filter(is_active = True)
    user = request.user
    context = {'list': list,'user':user}
    return render(request, get_html('sop.html'), context)

@login_required(login_url='/admin/login/?next=/')
def sop_id(request,id):
    # app ={'app':'portal','disp':'信息系統入口','note':'頂層目錄'}
    # app['note']='頂層目錄'
    obj = SOP.objects.filter(is_active = True,id=id)[0]
    key ={"name":obj.name}
    list = SOPDetail.objects.filter(sop__id = id).order_by('seq')
    user = request.user
    context = {'obj': obj,'key': key,'list': list,'user':user}
    return render(request, get_html('sop_id.html'), context)


# https://stackoverflow.com/questions/1810891/django-how-to-filter-users-that-belong-to-a-specific-group
# This is a really old question, but for those googling the answer to this (like I did), please know that the accepted answer is no longer 100% correct. A user can belong to multiple groups, so to correctly check if a user is in some group, you should do:

# qs = User.objects.filter(groups__name__in=['foo'])
# Of course, if you want to check for multiple groups, you can add those to the list:

# qs = User.objects.filter(groups__name__in=['foo', 'bar'])


@login_required(login_url='/admin/login/?next=/')
def mark(request):
    app ={'app':'portal','disp':'用戶權限','note':'頂層目錄'}
    # app['note']='頂層目錄'
    # list = User.objects.all().order_by('username')
    # list = User.objects.filter(is_superuser = True,is_staff = True, is_active = True).order_by('username')
    list = User.objects.filter(is_staff = True, is_active = True).order_by('username')
    
    list2 =Group.objects.all()
    # https://stackoverflow.com/questions/1251692/how-to-enumerate-an-objects-properties-in-python  
    # for x in list2:
    #     print(x.__dict__)
    
    # for x in list:
    #     # print("===",x.first_name,"===")
    #     temp =''
    #     for g in x.groups.all():
    #         print(g.name)
    #         temp += g.name +','
    #     # print(l)
    #     x.groups = temp

    user = request.user
    group = 'dev'
    
    grp_list = Group.objects.all()
    # print("xxx",grp)
    for x in grp_list:
        # print(x)
        usr_list = User.objects.filter(groups__name__in=[x])
        # print("===")
        # print(usr)
        # print("===")
        x.user_list = usr_list
        # print(usr_list.__dict__)
        
    

    

    context = {'app': app,'grp_list': grp_list,'list': list,'user':user}
    # print(user)
    # print(group)
    
    if is_user_in_group(user,group) == False:
        return render(request, get_html('auth.html'), context)
    
    return render(request, get_html('user_group.html'), context)


@login_required(login_url='/admin/login/?next=/')
def permission(request):
    app ={'app':'portal','disp':'用戶權限','note':'頂層目錄'}
    # app['note']='頂層目錄'
    # list = User.objects.all().order_by('username')
    # list = User.objects.filter(is_superuser = True,is_staff = True, is_active = True).order_by('username')
    list = User.objects.filter(is_staff = True, is_active = True).order_by('username')
    
    list2 =Group.objects.all()
    # https://stackoverflow.com/questions/1251692/how-to-enumerate-an-objects-properties-in-python  
    # for x in list2:
    #     print(x.__dict__)
    
    # for x in list:
    #     # print("===",x.first_name,"===")
    #     temp =''
    #     for g in x.groups.all():
    #         print(g.name)
    #         temp += g.name +','
    #     # print(l)
    #     x.groups = temp

    user = request.user
    group = 'dev'
    
    grp_list = Group.objects.all()
    # print("xxx",grp)
    for x in grp_list:
        # print(x)
        usr_list = User.objects.filter(groups__name__in=[x])
        # print("===")
        # print(usr)
        # print("===")
        x.user_list = usr_list
        # print(usr_list.__dict__)
        
    

    

    context = {'app': app,'grp_list': grp_list,'list': list,'user':user}
    # print(user)
    # print(group)
    
    # if is_user_in_group(user,group) == False:
    #     return render(request, get_html('auth.html'), context)
    
    app = 'portal'
    page = 'permission'

    if not is_user_app_page(user,app,page):
        context={'user':user,'app':app,'page':page}
        return render(request, get_html('no_user_app_page.html'), context)
    


    # return render(request, get_html('user_group.html'), context)
    return render(request, get_html('permission.html'), context)

@login_required(login_url='/admin/login/?next=/')
def apppagegrp(request):
    user = request.user
    app = 'portal'
    page = 'apppagegrp'

    list = AppPageAuthGrp.objects.all()
    

    

    context = {'app': app,'list': list,'user':request.user}
    # print(user)
    # print(group)
    
    # if is_user_in_group(user,group) == False:
    #     return render(request, get_html('auth.html'), context)
    
    
    if not is_user_app_page(user,app,page):
        context={'user':user,'app':app,'page':page}
        return render(request, get_template_no_user_app_page(), context)
    


    return render(request, get_html('apppagegrp.html'), context)



@login_required(login_url='/admin/login/?next=/')
def test001(request):
    user = request.user
    app = 'portal'
    page = 'apppagegrp'

    list = AppPageAuthGrp.objects.all()
    

    

    context = {'app': app,'list': list,'user':request.user}
    # print(user)
    # print(group)
    
    # if is_user_in_group(user,group) == False:
    #     return render(request, get_html('auth.html'), context)
    
    
    if not is_user_app_page(user,app,page):
        context={'user':user,'app':app,'page':page}
        return render(request, get_template_no_user_app_page(), context)
    


    return render(request, get_html('test001.html'), context)


@login_required(login_url='/admin/login/?next=/')
def case001(request):
    user = request.user
    app = 'portal'
    page = 'apppagegrp'

    list = Note.objects.filter(grp = 'case001').order_by('seq')
    

    

    context = {'app': app,'list': list,'user':request.user}
    # print(user)
    # print(group)
    
    # if is_user_in_group(user,group) == False:
    #     return render(request, get_html('auth.html'), context)
    
    
    if not is_user_app_page(user,app,page):
        context={'user':user,'app':app,'page':page}
        return render(request, get_template_no_user_app_page(), context)
    


    return render(request, get_html('case001.html'), context)

@login_required(login_url='/admin/login/?next=/')
def aliyun001(request):
    user = request.user
    app = 'portal'
    page = 'apppagegrp'

    list = Note.objects.filter(grp = 'aliyun001').order_by('seq')
    

    

    context = {'app': app,'list': list,'user':request.user}
    # print(user)
    # print(group)
    
    # if is_user_in_group(user,group) == False:
    #     return render(request, get_html('auth.html'), context)
    
    
    if not is_user_app_page(user,app,page):
        context={'user':user,'app':app,'page':page}
        return render(request, get_template_no_user_app_page(), context)
    


    return render(request, get_html('aliyun001.html'), context)

@login_required(login_url='/admin/login/?next=/')
def it(request):
    user = request.user
    app = 'portal'
    page = 'apppagegrp'

    list = Note.objects.filter(grp = 'it').order_by('seq')
    context = {'app': app,'list': list,'user':request.user}
    
    if not is_user_app_page(user,app,page):
        context={'user':user,'app':app,'page':page}
        return render(request, get_template_no_user_app_page(), context)
    
    return render(request, get_html('it.html'), context)

@login_required(login_url='/admin/login/?next=/')
def wp(request):
    user = request.user
    app = 'portal'
    page = 'apppagegrp'

    list = Note.objects.filter(grp = 'wp').order_by('seq')
    context = {'app': app,'list': list,'user':request.user}
    
    if not is_user_app_page(user,app,page):
        context={'user':user,'app':app,'page':page}
        return render(request, get_template_no_user_app_page(), context)
    
    return render(request, get_html('wp.html'), context)

@login_required(login_url='/admin/login/?next=/')
def django(request):
    user = request.user
    app = 'portal'
    page = 'apppagegrp'

    list = Note.objects.filter(grp = 'django').order_by('seq')
    context = {'app': app,'list': list,'user':request.user}
    
    if not is_user_app_page(user,app,page):
        context={'user':user,'app':app,'page':page}
        return render(request, get_template_no_user_app_page(), context)
    
    return render(request, get_html('django.html'), context)


@login_required(login_url='/admin/login/?next=/')
def case002(request):
    user = request.user
    app = 'portal'
    page = 'apppagegrp'

    list = Note.objects.filter(grp = 'case002').order_by('seq')
    

    

    context = {'app': app,'list': list,'user':request.user}
    # print(user)
    # print(group)
    
    # if is_user_in_group(user,group) == False:
    #     return render(request, get_html('auth.html'), context)
    
    
    if not is_user_app_page(user,app,page):
        context={'user':user,'app':app,'page':page}
        return render(request, get_template_no_user_app_page(), context)
    


    return render(request, get_html('case002.html'), context)


def get_parttime(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, get_html('get_parttime.html'), {'form': form})

def get_part(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PartForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PartForm()

    return render(request, get_html('get_part.html'), {'form': form})

def get_part2(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PartForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PartForm()

    return render(request, get_html('get_part.html'), {'form': form})


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, get_html('name.html'), {'form': form})




def your_name(request):
    def gen_excel_fordownload():
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print(BASE_DIR)

        STATIC_ROOT = os.path.join(BASE_DIR, 'static')
        PARTTIME_ROOT = os.path.join(STATIC_ROOT, 'parttime')
        
        print(STATIC_ROOT)
        print(PARTTIME_ROOT)

        corename ='hello'
        shortname  = corename +"_"+str(time.time())+".xlsx"
        filename = os.path.join(PARTTIME_ROOT,shortname )
        
        
        # filename ='/Users/pinglingchen/19/django2019.com/mysite001/km001/static/hello.xlsx'
        workbook = xlsxwriter.Workbook(filename)
        worksheet = workbook.add_worksheet()

        worksheet.write('A1', 'Hello world')

        workbook.close()
        return render(request, get_html('your_name.html'), {'shortname': shortname,'filename': filename})




    if request.method == 'POST':
        return gen_excel_fordownload()
        # print("what? it's post ")
    else:
        print("NOT POST  ")
        return render(request, get_html('what.html'))




