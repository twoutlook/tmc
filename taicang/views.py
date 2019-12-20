from django.shortcuts import render
from .models import Ticket
from django.db.models import Count, Sum, Max, Min



from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm
from .forms import PhoneForm\

app = 'taicang'
def getHtml(html):
    return app+'/'+html+'.html'

def index(request):
    # list1 = Meeting.objects.values('date1').annotate(headcnt=Count('name'))
   
    context = {'list1': None}
    return render(request, getHtml('index'), context)

def sum1(request):
    sum1 = Ticket.objects.values('club','feetxt').annotate(idcnt=Count('id'))
   
    context = {'sum1': sum1}
    return render(request, getHtml('sum1'), context)



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

    return render(request, getHtml('name'), {'form': form})

def input_phone(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PhoneForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PhoneForm()

    return render(request, getHtml('input_phone'), {'form': form})

def phone_result(request):
    sum1 = Ticket.objects.values('club','feetxt').annotate(idcnt=Count('id'))
    if request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            
            list1 = Ticket.objects.filter(phone=phone)


            context = {'list1': list1,'phone': phone}
            return render(request, getHtml('phone_result'), context)

        
    else:
        print("NO, need to redirect it!")

    return HttpResponseRedirect('../')
    # context = {'sum1': sum1}
    # return render(request, getHtml('sum1'), context)
